import gc, weakref, threading
import struct, array
import time, datetime
import numpy as np


def soft_quit():
    import os
    #os.kill(os.getpid(), 15)
    os.kill(os.getpid(), 2)

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m%d %H:%M:%S")

def get_date_string():
    return datetime.datetime.now().strftime("%Y%m%d")

def get_time_string():
    return datetime.datetime.now().strftime("%H%M%S")

def get_datetime_string():
    return datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

def get_datetime():
    return datetime.datetime.now()

def create_thread(target, args=()):
    """Create new thread for execution."""
    thread = threading.Thread(target=target, args=args)

