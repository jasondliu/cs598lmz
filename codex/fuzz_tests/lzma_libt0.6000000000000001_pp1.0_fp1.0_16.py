import lzma
lzma.LZMACompressor()

import copyreg
copyreg.pickle(type(lambda: 0), lambda obj: (lambda: 0, ()))

import marshal
marshal.dumps(0)

import math
math.atan2(0,0)

import mmap
mmap.mmap(-1,0)

import nt
nt.R_OK

import operator
operator.__abs__(0)

import os
os.__all__

import parser
parser.expr('0')

import py_compile
py_compile.compile('')

import selectors
selectors.DefaultSelector()

import socket
socket.gethostbyname('localhost')

import struct
struct.__doc__

import subprocess
subprocess.Popen(['echo', 'Hello World'])

import sys
sys.__stderr__

import tempfile
tempfile.mkdtemp()

import threading
threading.Thread()

import time
time.sleep(0)

import timeit
time
