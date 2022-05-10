import select
# Test select.select
#select.select([], [], [], 0)
print 'select.select():', select.select([], [], [], 0)


import os
import sys
import time
import select
import binascii
import fcntl

import fcntl
import termios
import array
import struct

#source: http://stackoverflow.com/questions/1111056/how-not-to-block-application-when-using-serial-port
def getKey():
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, old
