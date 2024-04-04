import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # ノードの生成に利用
from std_msgs.msg import String # メッセージ：文字列
class MinimalPublisher(Node): # Nodeのサブクラス
   def __init__(self): # コンストラクタ
      super().__init__('minimal_publisher') # 初期化
      # 'topic'トピック（文字列）をPublishするPublisher
      self.publisher_ = self.create_publisher(String, 'topic', 10)
      timer_period = 0.5  # seconds
      # タイマーを生成
      self.timer = self.create_timer(timer_period,self.timer_callback)
      self.i = 0
   def timer_callback(self): # コールバック関数 0.5秒ごと
      msg = String()
      msg.data = 'Hello World: %d' % self.i # データを準備
      self.publisher_.publish(msg) # Publishを実行
      self.get_logger().info('Publishing: "%s"' % msg.data)
      self.i += 1
   def main(args=None):
      rclpy.init(args=args) # ライブラリを初期化
      minimal_publisher = MinimalPublisher() # ノードを生成
      rclpy.spin(minimal_publisher) # callback関数が呼ばれる
      minimal_publisher.destroy_node()
      rclpy.shutdown()
if __name__ == '__main__':
      main()


