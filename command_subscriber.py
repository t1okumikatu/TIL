import rclpy
from rclpy.node import Node
#from std_msgs.msg import String
from geometry_msgs.msg import Twist

class CommandSubscriber(Node):
    def __init__(self):
        super().__init__('command_subscriber_node')
        self.subscription=self.create_subscription(Twist,'cmd_vel',self.listener_callback,10)
        self.subscription  #prevent
    def listener_callback(self,Twist):
        self.get_logger().info(f'並進速度＝{Twist.linear.x}角速度＝{Twist.angular.z}')
def main(args=None):
    rclpy.init(args=args)
    command_subscriber=CommandSubscriber()
    rclpy.spin(command_subscriber)
    #Destroy the node explicitly
    #(optional-otherwise it will be done automaticaly
    #when the garbage collector destroys the node object
    command_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
