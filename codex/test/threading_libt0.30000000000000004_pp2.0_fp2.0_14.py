import threading
threading.Thread(target=lambda: None).start()

import time
time.sleep(1)

import sys
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
### Disinfection
#################################
