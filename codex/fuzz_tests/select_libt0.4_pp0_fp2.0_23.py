import select
import sys
import termios
import tty
import time
import math

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def getAngle(x,y):
    angle = math.atan2(y,x)
    angle = math.degrees(angle)
    if angle < 0:
        angle += 360
    return angle

def getDistance(x,y):
    return math.sqrt(x*x + y*y)

def getCommand(x,y,angle):
    distance = getDistance(x,y)
    angle = getAngle(x,y)
    return "!G 1 " + str(angle) + " " + str(distance)

def getCommand2(x,y,angle):
    distance = getDistance(x,y)

