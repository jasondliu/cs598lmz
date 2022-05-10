import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import sqlite3
conn = sqlite3.connect('db/mydb.db')
c = conn.cursor()


# ===========
# = Settings =
# ===========

# General settings
RUN_IN_BACKGROUND = True

# Thresholds
# Maximum allowed distance between two face detections (in pixels)
THRESHOLD_FACE_DISTANCE = 150
# Maximum allowed time between two face detections (in seconds)
THRESHOLD_FACE_TIME = 3

# Thread settings
# Frequency to analyze the webcam image in FPS (frames per second)
THREAD_FREQUENCY = 2

# Haar cascade settings
# Haar cascade classifier XML file path
HAAR_FILE = 'haarcascade_frontalface_default.xml'

# ========
# = Code =
# ========

# Lock to control the access to the shared resources
lock = threading.Lock()

# Load the Haar cascade file
haar = cv2.CascadeClassifier(HAAR_FILE)

# Initialize the first frame and the list
