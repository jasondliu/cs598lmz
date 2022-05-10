import select
import termios
import signal
import random
import sys
import argparse
import readline
from irc import sendsay, waitmsg

def getch():
   fd = sys.stdin.fileno()
   old = termios.tcgetattr(fd)
   new = termios.tcgetattr(fd)
   new[3] = new[3] & ~termios.ICANON
   try:
      termios.tcsetattr(fd, termios.TCSANOW, new)
      chr = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSANOW, old)
   return chr

def getche():
   chr = getch()
   sys.stdout.write(chr)
   sys.stdout.flush()
   return chr

def sendmsg(msg):
   sendsay(user, chan, msg)
