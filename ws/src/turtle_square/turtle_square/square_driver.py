import math

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from geometry_msgs.msg import Twist


class SquareDriver(Node):
    def __init__(self):
        super().__init__('square_driver')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.side_time = 2.0                                  # how many seconds it's going straight
        self.turn_speed = 1.0                                 # rotational speed [rad/s]
        self.turn_time = (math.pi / 2) / self.turn_speed      # rotation time of 90 degrees

        self.state = 'forward'
        self.state_start = self.get_clock().now()
        self.timer = self.create_timer(0.1, self.loop)        # loop() 10 times per second
        self.get_logger().info('I am going around the square!')

    def loop(self):
        elapsed = (self.get_clock().now() - self.state_start).nanoseconds / 1e9
        msg = Twist()

        if self.state == 'forward':
            msg.linear.x = 1.0
            if elapsed >= self.side_time:
                self.switch('turn')
        else:
            msg.angular.z = self.turn_speed
            if elapsed >= self.turn_time:
                self.switch('forward')

        self.publisher.publish(msg)

    def switch(self, new_state):
        self.state = new_state
        self.state_start = self.get_clock().now()


def main():
    rclpy.init()
    node = SquareDriver()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
