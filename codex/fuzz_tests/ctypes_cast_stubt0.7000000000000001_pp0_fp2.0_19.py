import ctypes
ctypes.cast(1, ctypes.py_object)

#import subprocess
#subprocess.Popen("/bin/echo Hello")

import os
os.system("echo hello")

#import glob
#glob.glob("*")

import re
re.compile("python")

import calendar
calendar.isleap(2014)

import zlib
zlib.compress("hello")

import time
time.ctime(time.time())

import random
random.choice([1, 2, 3, 4])

#import socket
#socket.socket(socket.AF_INET, socket.SOCK_STREAM)

import hashlib
hashlib.md5("hello").digest()

import struct
struct.pack(">i4sh", 7, "spam", 8)

import datetime
datetime.date.today()

import cmath
cmath.sin(cmath.pi / 4)

import math
math.sin(math.pi / 4)

#import __hello__
#hello

import cPickle
c
