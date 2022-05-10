import select
import sys
import time
import tty
import termios

# ROS
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

# Custom
import message_queue

# Global variables

# Key mapping
key_mapping = {
    'w': [0, 1],
    'x': [0, -1],
    'a': [1, 0],
    'd': [-1, 0],
    's': [0, 0]
}

# Twist message
twist = Twist()

# Message queue
queue = message_queue.MessageQueue()

# Keyboard input
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)


def get_key():
    """
    Gets keyboard input
    :return:
    """
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.
