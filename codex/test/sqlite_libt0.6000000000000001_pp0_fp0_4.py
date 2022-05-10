import ctypes
import ctypes.util
import threading
import sqlite3
import time
import logging
import os
import sys

def create_logger(name, log_file, level=logging.INFO, stream=sys.stdout):
    """Function setup as many loggers as you want"""
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

def get_serial_port():
    """Function to find the serial port"""
    # Find the serial port
    serial_port = None
    serial_port_candidates = glob.glob('/dev/ttyUSB*') # List of candidates
    if len(serial_port_candidates) > 0:
        serial_port = serial_port_candidates[0] # We take the first
