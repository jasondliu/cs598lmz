import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)

import os
# Test os.O_CREAT

import random
# Test random.randint(0, 1)

import re
# Test re.compile(r'\d+')

import select
# Test select.select([], [], [])

import socket
# Test socket.socket(socket.AF_INET, socket.SOCK_STREAM)

import struct
# Test struct.unpack('i', '\x00\x00\x00\x00')

import subprocess
# Test subprocess.Popen(['ls', '-l'])

import sys
# Test sys.stdout.write('hello\n')

import threading
# Test threading.Thread(target=lambda: None)

import time
# Test time.sleep(0.1)

import traceback
# Test traceback.format_exc()

import types
# Test types.ClassType

import unittest
# Test unittest.TestCase

import urllib
