import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import random

class LightSource(Node):
    def __init__(self):
        super().__init__('light_source')
        self.publisher = self.create_publisher(Point, 'light_position', 10)
        self.timer = self.create_timer(2.0, self.publish_light_position) 

    def publish_light_position(self):
        msg = Point()
        msg.x = random.uniform(0.0, 11.0)
        msg.y = random.uniform(0.0, 11.0)
        msg.z = 0.0
        self.publisher.publish(msg)
        self.get_logger().info(f'Light position: ({msg.x}, {msg.y})')

def main():
    rclpy.init()
    node = LightSource()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

