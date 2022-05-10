import mmap
# Test mmap.mmap(0, 1, "sharedmem")

import os
# Test os.getpid()

import re
# Test re.compile("a")

import select
# Test select.select([], [], [], 0)

import socket
# Test socket.socket().bind(("", 0))

import subprocess
# Test subprocess.Popen(["echo"], stdout=subprocess.PIPE).communicate()

import sys
# Test sys.getrefcount(1)

import tempfile
# Test tempfile.mkstemp()

import threading
# Test threading.Thread(target=lambda: None).start()

import time
# Test time.time()

import traceback
# Test traceback.extract_stack()

import types
# Test types.FunctionType(lambda: None, globals(), "")

import unittest
# Test unittest.TestCase().assertTrue(True)

import urllib
# Test urllib.urlopen("http://www.python.org/")

import urlparse
# Test urlparse
