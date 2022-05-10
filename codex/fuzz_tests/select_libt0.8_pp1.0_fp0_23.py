import select,sys
import tty, termios
from geometry_msgs.msg import PoseStamped

def send_goal(x, y, z):
	try:
		# Subscribe to the move_base action server
		move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
				
		# Wait 60 seconds for the action server to become available
		move_base.wait_for_server(rospy.Duration(60))
				
		# Creates a goal to send to the action server.
		goal = MoveBaseGoal()
		goal.target_pose.header.frame_id = "map"
		goal.target_pose.header.stamp = rospy.Time.now()
				 
		# Move 0.5 meters forward along the x axis of the "map" coordinate frame 
		goal.target_pose.pose.position.x = x
		# Move 0.5 meters forward along the y axis of the "map" coordinate frame 
		goal.target_pose
