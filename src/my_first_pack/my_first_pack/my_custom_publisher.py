import rclpy as rp
from rclpy.node import Node
from geometry_msgs.msg import Twist
import threading


class TurtlesimPublisher(Node):
    def __init__(self):
        super().__init__('turtlesim_publisher')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.direction = None  # 입력 저장
        self.timer = self.create_timer(0.1, self.timer_callback)

        # 별도 스레드에서 사용자 입력 받기
        input_thread = threading.Thread(target=self.get_input)
        input_thread.daemon = True
        input_thread.start()

    def get_input(self):
        """사용자 키보드 입력을 받는 스레드"""
        while True:
            direction = input('방향 입력 (w:앞, s:뒤, a:좌, d:우, q:종료): ')
            if direction == 'q':
                print("프로그램 종료 중...")
                rp.shutdown()   # ROS 종료
                break
            elif direction in ['w', 's', 'a', 'd']:
                self.direction = direction
            else:
                print("잘못된 입력입니다.")

    def timer_callback(self):
        """현재 방향에 맞게 주기적으로 명령 발행"""
        msg = Twist()

        if self.direction == 'w':
            msg.linear.x = 1.0
        elif self.direction == 's':
            msg.linear.x = -1.0
        elif self.direction == 'a':
            msg.angular.z = 1.0
        elif self.direction == 'd':
            msg.angular.z = -1.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher.publish(msg)


def main(args=None):
    rp.init(args=args)
    node = TurtlesimPublisher()
    rp.spin(node)
    node.destroy_node()
    # rp.shutdown()


if __name__ == '__main__':
    main()









# import rclpy as rp
# from rclpy.node import Node

# from geometry_msgs.msg import Twist

# class TurtlesimPublisher(Node):
    
#     def __init__(self):
#         super().__init__('turtlesim_publisher')
#         self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
#         timer_period = 1.0
#         self.timer = self.create_timer(timer_period, self.timer_callback)
#         self.direction = None  # 현재 방향 저장 변수
    
#     def timer_callback(self):
#         msg = Twist()
#         while True:
#             direction = input('방향 입력 (w:앞, s:뒤, a:좌, d:우, q:종료): ')
#             if direction == 'q':
#                 break

#             if direction == 'w':
#                 msg.linear.x = 1.0
#             elif direction == 's':
#                 msg.linear.x = -1.0
#             elif direction == 'a':
#                 msg.angular.z = 1.0
#             elif direction == 'd':
#                 msg.angular.z = -1.0
#             else:
#                 print("잘못된 입력입니다.")

#             self.publisher.publish(msg)


# def main(args=None):
#     rp.init(args=args)

#     turtlesim_publisher = TurtlesimPublisher()
#     rp.spin(turtlesim_publisher)

#     turtlesim_publisher.destroy_node()
#     rp.shutdown()

# if __name__ == '__main__':
#     main()
