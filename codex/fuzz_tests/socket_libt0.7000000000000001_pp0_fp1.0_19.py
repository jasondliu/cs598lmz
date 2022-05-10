import socket
import os
import time

from contextlib import closing

from multitracking import Track, Tracks
from multitracking.helper import *
from multitracking.logger import *

# logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M')

class Tracker2D(object):
    """
    Tracker2D: A simple 2D tracker

    """

    def __init__(self, src, port=8000, show=True, debug=False, max_age=30, min_hits=2, iou_thresh=0.25, save_dir='.', min_area = 0.0, max_area = 40000):
        self.src = src
        self.host = ''
        self.port = port
        # self.recording = False
        self.data = b''
        self.data_len = 0
        self.show = show
        self.debug = debug
