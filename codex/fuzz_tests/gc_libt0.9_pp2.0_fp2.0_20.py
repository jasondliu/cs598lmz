import gc, weakref
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, EVENT_TYPE_MODIFIED, EVENT_TYPE_DELETED
from watchdog.events import EVENT_TYPE_MOVED, EVENT_TYPE_CREATED

import numpy as np

from doptrack.utils import LOG, LOG_ERROR

import time


class LabjackDataHandler(object):
    '''
    Handles the reading of a data file from a Labjack device
    '''
    
    def __init__(self, log_file, callback_on_update, callback_on_new_file=None, read_file=True, use_watchdog=True, use_tail=True):
        
        self.log_file = log_file
        self.callback_on_update = callback_on_update
        self.callback_on_new_file = callback_on_new_file
        self.read_file = read_file
        self.cols = 3
        self.total_lines = 0
        self.data = []
        
        self.file_last_modified_
