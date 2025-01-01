import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist
import math

class LightFollower(Node):
    def __init__(self):
        super().__init__('light_follower')
        self.subscription = self.create_subscription(
            Point, 'sensor_data', self.light_callback, 10)
        self.pose_subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.light_position = None
        self.turtle_pose = None

    def light_callback(self, msg):
        # Met à jour la position de la lumière
        self.light_position = msg
        self.update_movement()

    def pose_callback(self, msg):
        # Met à jour la position de la tortue
        self.turtle_pose = msg
        self.update_movement()

    def update_movement(self):
        # Vérifie si les positions sont valides
        if self.light_position is None or self.turtle_pose is None:
            return

        # Calcul de la distance entre la tortue et la lumière
        dx = self.light_position.x - self.turtle_pose.x
        dy = self.light_position.y - self.turtle_pose.y
        distance = math.sqrt(dx**2 + dy**2)

        # Calcul de l'angle entre la tortue et la lumière
        target_angle = math.atan2(dy, dx)
        angle_difference = target_angle - self.turtle_pose.theta

        # Normaliser l'angle
        angle_difference = math.atan2(math.sin(angle_difference), math.cos(angle_difference))

        # Création du message de commande de vitesse
        twist = Twist()

        if distance > 0.1:  # Si la tortue est proche, elle arrête de bouger
            twist.linear.x = min(2.0, distance)  # Limite la vitesse linéaire
            twist.angular.z = angle_difference * 4.0  # Contrôle proportionnel pour la rotation
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0

        # Publication de la commande de vitesse
        self.publisher.publish(twist)
        self.get_logger().info(
            f'Moving to light: Distance={distance:.2f}, Angle={angle_difference:.2f}')

def main():
    rclpy.init()
    node = LightFollower()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
