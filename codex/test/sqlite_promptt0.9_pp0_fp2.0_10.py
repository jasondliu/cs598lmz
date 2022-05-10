import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file:home/ec2-user.sqlite3?mode=ro", uri=true)

#import pylab
import numpy as np
import matplotlib.pyplot as plt
import barracuda

#import time

#-----------------------------------------------------
# Global variables
#-----------------------------------------------------

_msgs = {}
_msgs["show_available_messages"] = "[msg show_available_messages]"
_msgs["toggle_logging"] = "[msg toggle_logging]"
_msgs["position_logged"] = "position_logged"
_msgs["start_position_logging"] = "[msg start_position_logging 0]"
_msgs["stop_position_logging"] = "[msg stop_position_logging]"
_msgs["start_position_logging_frame"] = "[msg start_position_logging_frame]"
_msgs["stop_position_logging_frame"] = "[msg stop_position_logging_frame]"
