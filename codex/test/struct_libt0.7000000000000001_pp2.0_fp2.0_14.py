import _struct
import os
import sys
import urllib2
import time
from collections import deque
from struct import *

# The heart of the app
class TAPP:
    def __init__(self):
        self.start_time = time.clock()
        self.last_time = time.clock()
        self.last_second = self.last_time
        self.current_fps = 0
        self.current_fps2 = 0
        self.frames = 0
        self.frames2 = 0
        self.fps_list = deque()
        self.fps_list.extend([60])
        self.fps_list2 = deque()
        self.fps_list2.extend([60])
        self.downloads_list = []
        self.downloads_list_size = 0
        self.downloads_list_size_remain = 0
        self.downloads_list_size_total = 0
        self.downloads_list_size_total_remain = 0
        self.downloads_list_size_total_remain2 = 0
