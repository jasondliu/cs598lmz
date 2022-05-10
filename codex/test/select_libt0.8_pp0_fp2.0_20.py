import select_data


import sys
import time
import os

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler



class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.json"]

