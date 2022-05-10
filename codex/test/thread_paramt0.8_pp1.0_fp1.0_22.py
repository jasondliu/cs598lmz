import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()


import rospy

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.msg import Pose

class controller():
	def __init__(self):
		self.sub_pose = rospy.Subscriber("turtle1/pose",Pose,self.pose_callback)
		self.sub_cmdvel = rospy.Subscriber("turtle1/cmd_vel",Twist,self.cmdvel_callback)
		self.pub_vel = rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)
		self.vel_msg = Twist()
		self.pose = Pose()
		self.cmdvel = Twist()
		self.Kp = 3.14159/2.0

	def pose_callback(self,pose):
		self.pose = pose

	def cmdvel_callback(self,cmdvel):
		self.cmdvel = cmdvel

