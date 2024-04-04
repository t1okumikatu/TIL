from robot_interfaces.srv import RobotCommand
import rclpy
from rclpy.node import Node
import pigpio
import threading
class RobotService(Node):
    target_speed_R=0.0
    target_speed_L=0.0
    def __init__(self):
      super().__init__('robot_service')
      self.srv=self.create_service(RobotCommand,'robot_command',self.robot_command_callback) #サービスの生成
    def robot_command_callback(self,request,response):
      global count_R
      global count_L
      responese.done=False
      count_R=0
      count_L=0
      self.target_speed_R=0.3  #目標速度設定
      self.target_speed_L=0.3
      while count_R < request.dist: #目標距離達成まで待機
         pass
      self.target_speed_R=0.0 #モーター停止＆初期化
      self.target_speed_L=0.0
      pi.set_PWM_dutycycle(MOT_R_1,0)
      pi.set_PWM_dutycycle(MOT_R_2,0)
      init_variables_R()
      pi.set_PWM_dutycycle(MOT_L_1,0)
      pi.set_PWM_dutycycle(MOT_L_2,0)
      init_variables_L()
      response.done=True #レスポンス送信
      return response




robot_service=None
def main(args=None):
    global robot_service
#    pi.set_PWM_dutycycle(MOT_R_1,0)
 #   pi.set_PWM_dutycycle(MOT_R_2,0)
  #  pi.set_PWM_dutycycle(MOT_L_1,0)
   # pi.set_PWM_dutycycle(MOT_L_2,0)
    rclpy.init(args=args)
    robot_service=RobotService()
    drive()
    rclpy.spin(robot_service)
    robot_service.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()
