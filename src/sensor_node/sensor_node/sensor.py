import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.subscription = self.create_subscription(
            Point, 'light_position', self.callback, 10)
        self.publisher = self.create_publisher(Point, 'sensor_data', 10)

    def callback(self, msg):
        self.publisher.publish(msg)
        self.get_logger().info(f'Sensor data: ({msg.x}, {msg.y})')

def main():
    rclpy.init()
    node = SensorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

