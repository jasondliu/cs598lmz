import ctypes
ctypes.cast(0, ctypes.py_object).value = None
## finish initializing

from threading import Thread
from threading import Lock
from threading import Condition


#from collections import deque
