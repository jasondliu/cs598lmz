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
def Disinfect(speed):
	print "Disinfection"
	
	# Initialize robot
	robot = RobotControl()
	robot.Init()
	
	# Move to the first position
	robot.Move(0, 0, 0, speed, 0)
	
	# Move to the second position
	robot.Move(0, 0, 0, speed, 0)
	
	# Move to the third position
	robot.Move(0, 0, 0, speed, 0)
	
	# Move to the fourth position
	robot.Move(0, 0, 0, speed, 0)
	
	# Move to the fifth position
	robot.Move(0, 0, 0, speed, 0)
	
	# Move to the sixth position
	ro
