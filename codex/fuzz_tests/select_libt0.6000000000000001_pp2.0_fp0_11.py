import select
import sys
import termios
import tty
import time
import threading

# Define the keyboard object
class Keyboard:
    def __init__(self):
        self.key = None
        self.key_dict = {
            'w' : 'up',
            'a' : 'left',
            's' : 'down',
            'd' : 'right',
            'q' : 'quit'
            }

    def getKey(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def readkey(self):
        self.key = self.getKey()

    def getChar(self):
        return self.key_dict.get(self.key, 'unknown')


# Define the obstacle
