import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

#from ctypes import cdll

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_now_time

# os.path.abspath(os.path.dirname(__file__))
print("os.path.abspath(os.path.dirname(__file__)):%s"%os.path.abspath(os.path.dirname(__file__)))

# os.path.abspath(os.path.dirname(__file__) + '/' + '..')
print("os.path.abspath(os.path.dirname(__file__) + '/' + '..'):%s"%os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

# os.path.abspath(__file__)
