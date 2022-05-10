import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()
import time


g.goal.goal_state.position.z = 4
g.goal.goal_state.position.y = -2

g.goal.goal_state.orientation.x = 0.70710678118
g.goal.goal_state.orientation.y = 0.0
g.goal.goal_state.orientation.z = 0.0
g.goal.goal_state.orientation.w = 0.70710678118

g.goal.max_velocity_scaling_factor = 1
g.goal.tolerance = 0.001
g.goal_time_tolerance = 0.001
g.path_tolerance = 0.001
g.goal.target_pose.header.frame_id = "panda_link0"
g.goal.target_pose.header.stamp = rospy.Time.now()



g.goal_constraints = JointConstraint()
g.goal_constraints.joint_name = "panda_joint1"
g.goal
