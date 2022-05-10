import select 
import sys
import termios
import tty
import pigpio
import time
import threading
import multiprocessing
import queue

pi = pigpio.pi()

# un-comment line below for dummy pi (pc)
#pi = pigpio.pi('localhost', 8888)

# Set these depending on your setup
leftA = 4
leftB = 17
leftPWM = 18

rightA = 23
rightB = 24
rightPWM = 25

# These are the power levels to use
# 0.0 - 1.0
# I found 0.5 to work well
# These are set so that the drive is stopped
# The PWM pins will be set to HIGH when the drive is
# moving forward and to LOW when the drive is 
# moving backwards
leftDrivePower = 0
rightDrivePower = 0

# initialize the PiGpio library
pi = pigpio.pi()

# set all the pins to output mode
pi.set_mode(leftA, pigpio.OUTPUT)
