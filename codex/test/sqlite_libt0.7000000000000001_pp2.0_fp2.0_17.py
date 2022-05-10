import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import signal
import socket
import copy
import traceback
import ConfigParser

from types import *
from optparse import OptionParser

from pymavlink import mavwp, mavutil
from pymavlink.rotmat import Vector3
from MAVProxy.modules.lib import mp_module

def parse_csv_line(line, param_types):
    '''parse a line of a CSV file'''
    line = line.strip()
    if line.startswith('#') or line.startswith(';'):
        return None
    parts = line.split(',')
    if len(parts) != len(param_types):
        return None
    param = []
    for (k, ptype) in enumerate(param_types):
        if ptype == 'int':
            param.append(int(parts[k]))
        else:
            param.append(float(parts[k]))
    return param

