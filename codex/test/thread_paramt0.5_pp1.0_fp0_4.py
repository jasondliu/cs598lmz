import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# import sys, termios, tty
# def getch():
#     fd = sys.stdin.fileno()
#     old_settings = termios.tcgetattr(fd)
#     try:
#         tty.setraw(sys.stdin.fileno())
#         ch = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#     return ch

# import curses
# def getch():
#     return curses.getch()

import os
def getch():
    return os.read(0,1)

import sys
def print_pos(x, y, string):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, string))
    sys.stdout.flush()

import random
