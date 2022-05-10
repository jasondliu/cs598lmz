import select
import sys
import termios
import tty
import time
import threading

from evdev import InputDevice, categorize, ecodes, KeyEvent

import rospy
from std_msgs.msg import Int16

# This function was taken from the internet
# Source: http://stackoverflow.com/questions/2408560/python-nonblocking-console-input
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# This function was taken from the internet
# Source: http://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
   
