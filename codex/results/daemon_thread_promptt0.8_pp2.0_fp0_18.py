import threading
# Test threading daemon
def my_function():
    print("Hello!")
threading.Thread(target=my_function).start()

# Test log file writing
import time
import sys
from timeit import default_timer as timer
import logging
import os

# Configure logger
logger = logging.getLogger('sift_logger')
logger.setLevel(logging.DEBUG)
fname = "sift_log.txt"
ftype = "a"
fh = logging.FileHandler(fname, mode=ftype)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Write to log file
logger.info("Test")
logger.info("Test")
logger.info("Test")
logger.info("Test")

# Test object detection
from object_detector import ObjectDetector

# Test streamer
