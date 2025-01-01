import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from turtlesim.srv import TeleportAbsolute

class LightIndicator(Node):
    def __init__(self):
        super().__init__('light_indicator')
        self.subscription = self.create_subscription(
            Point, 'light_position', self.update_light_position, 10)
        self.cli = self.create_client(TeleportAbsolute, '/light/teleport_absolute')

    def update_light_position(self, msg):
        if not self.cli.service_is_ready():
            self.cli.wait_for_service()

        req = TeleportAbsolute.Request()
        req.x = msg.x
        req.y = msg.y
        req.theta = 0.0

        self.cli.call_async(req)
        self.get_logger().info(f'Updated light position to ({msg.x:.2f}, {msg.y:.2f})')

def main():
    rclpy.init()
    node = LightIndicator()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
