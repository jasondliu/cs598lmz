import gc, weakref
import alsaaudio
import time
import subprocess
import threading
import numpy as np
from time import sleep
from subprocess import Popen, PIPE
from threading import Thread, Lock
from multiprocessing import Process, Pipe
from os.path import expanduser
from os import unlink
from datetime import datetime
from multiprocessing import Pool
from multiprocessing import Process, Queue
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double
from ctypes import c_char_p, c_double, c_int
from ctypes import cdll
from ctypes import c_char_p, c_double, c_int, c_void_p
from ctypes import c_void_p, c_int, c_char_p
from ctypes import c_size_t, c_void_p, c_char_p, c_int
from ctypes import byref, memmove, c_void_p, c_int, c_char_p
from ctypes import c_size_t, c_void
