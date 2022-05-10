import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start() # Toggle console output
# /Debug/

#---

from board import *
from ezblock import *
from ezbutton import *
from ezpwm import *
from ezled import *
from eztft import *
from ezpiezo import *
from ezsound import *
from ezultrasonic import *
from ezbuzzer import *
from ezinfrared import *
from ezlight import *
from ezknob import *
from ezpotentiometer import *
from ezflame import *
from ezjoystick import *
from eztemperature import *
from ezsoil import *
from ezdht11 import *
from ezserial import *
from ezultrasonic import *
from ezsensor import *

#---

class Sensor:
    def __init__(self):
        self.__init()
        self.__checkEnv() # Check if root
