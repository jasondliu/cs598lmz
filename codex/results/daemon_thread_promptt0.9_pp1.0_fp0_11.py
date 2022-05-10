import threading
# Test threading daemon
import dweepy

# Import all scripts
import drive
import avoid
import search

# Dweet for data
thing_name = 'dewbot'

# Distance sensor globals
distance_1 = 0
distance_2 = 0

# Front line Sensor globals
front_1 = 0
front_2 = 0

# Motor positions
POS_1 = 'Servo-A'
POS_2 = 'Servo-B'
FORWARD_LEFT = False
FORWARD_RIGHT = False
BACKWARD_LEFT = False
BACKWARD_RIGHT = False

# Motor constants
TURN_SPEED = 60
TRACK_WIDTH = 14 #inches


def read_sensors():
    # Read the distance sensors
    global distance_1
    global distance_2
    global front_1
    global front_2
    global FORWARD_LEFT
    global FORWARD_RIGHT
    global BACKWARD_LEFT
    global BACKWARD_RIGHT

    # Read the distance sensors
    distance_1 = int(tr.read_distance(0))

