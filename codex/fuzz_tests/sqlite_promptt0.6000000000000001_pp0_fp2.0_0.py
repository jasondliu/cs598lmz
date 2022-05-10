import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/dev/shm/test.db', check_same_thread=False)


class SharedDict(object):
    '''
    ctypes.sharedctypes.c_char_p()
    .value
    .value = 'str'
    '''
    def __init__(self, name, shared_dict, mode='r', lock=None):
        self.name = name
        self.shared_dict = shared_dict
        self.mode = mode
        self.lock = lock
    
    def __enter__(self):
        if self.lock:
            self.lock.acquire()
        return self
    
    def __exit__(self, type, value, tb):
        if self.lock:
            self.lock.release()
    
    def __getitem__(self, key):
        if key not in self.shared_dict:
            raise KeyError
        return self.shared_dict[key].value
    
    def __setitem__(self, key, value):
        if self.mode == 'r':
            raise Exception
