import select
import sys
import termios
import tty

import rospy
from std_msgs.msg import String

key_pub = rospy.Publisher('keys', String, queue_size=1)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('keyboard_driver')
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key_pub.publish(sys.stdin.read(1))
        rate.sleep()
