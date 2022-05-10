import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, fd)

import os
# Test os.open(filename, os.O_RDWR | os.O_CREAT)

import re
# Test re.compile(pattern)

import select
# Test select.select([], [], [], 0.1)

import signal
# Test signal.signal(signal.SIGUSR1, signal.SIG_IGN)

import socket
# Test socket.socket(socket.AF_INET, socket.SOCK_STREAM)

import struct
# Test struct.pack("i", 1)

import sys
# Test sys.stdout.write("hello\n")

import threading
# Test threading.Thread(target=lambda: None)

import time
# Test time.sleep(0.1)

import traceback
# Test traceback.format_exc()

import types
# Test types.FunctionType(lambda x: x, globals())

import unittest
# Test unittest.TestCase().assertE
