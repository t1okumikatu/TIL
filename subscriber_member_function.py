import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # ノードの生成に利用
from std_msgs.msg import String # メッセージ：文字列
class MinimalSubscriber(Node): # Nodeのサブクラ
   def __init__(self): # コンストラクタ
      super().__init__('minimal_subscriber') # 初期化
      # 'topic'トピック（文字列）をSubscribeするSubscriber
      self.subscription = self.create_subscription(String,'topic',self.listener_callback,10)
      self.subscription  # prevent unused variable warning
   def listener_callback(self, msg): # 受信時に呼ばれる
      self.get_logger().info('I heard: "%s"' % msg.data)
   def main(args=None):
      rclpy.init(args=args) # ライブラリを初期化
      minimal_subscriber = MinimalSubscriber() # ノードを生成
      rclpy.spin(minimal_subscriber) # callback関数が呼ばれる
      minimal_subscriber.destroy_node()
      rclpy.shutdown()
if __name__ == '__main__':
      main()


