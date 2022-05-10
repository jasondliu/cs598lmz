import ctypes
ctypes.cast(0, ctypes.py_object)

# If that does not cause an exception, then you have an issue with your Python
# installation.

# If you are running this script on a server, you probably want to remove the
# "interactive = True" option.

# Note that this script will not work with Python 2.

# Importing the main class
from pygazeanalyser.eyetracker import EyeTracker

# Setting up the display
DISPTYPE = 'pygame'
DISPSIZE = (800,600)
SCREENNR = 0

# Setting up the tracker
TRACKERTYPE = 'smi'
TRACKERDATA = 'sample.idf'

# Creating an instance of the main class
et = EyeTracker(trackertype=TRACKERTYPE, trackerdata=TRACKERDATA,
	disptype=DISPTYPE, dispsize=DISPSIZE, screennr=SCREENNR,
	eventdetection='native', saccade_velocity_threshold=35,
	saccade_acceleration_threshold=9000,
