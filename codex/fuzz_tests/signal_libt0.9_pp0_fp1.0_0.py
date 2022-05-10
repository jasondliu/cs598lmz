import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
sys.path.append('/usr/lib/python2.7/dist-packages')
sys.path.append('/usr/lib/python2.7/')
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
sys.path.append(r'/home/pi/droneponics')
sys.path.append(r'/home/pi/drone-crew')
sys.path.append(r'/home/pi/droneponics/components/')
sys.path.append(r'/home/pi/droneponics/gui/')

from OPi import GPIO

import datetime
import time
import grovepi
from drone import Drone

class Pump (Drone):

    def __init__(self, name, relay_gpio_pin , deviceType="pump" ,activeHigh=True):
        #make sure there is a config file
        Drone.__init__(self, name, deviceType )
        

