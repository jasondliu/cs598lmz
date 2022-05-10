import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno
import array
import struct
import fcntl
import subprocess
import time

import test.support
from test.support import TESTFN, unlink, run_unittest, import_module

# Skip test if there is no if_indextoname()
try:
    socket.if_indextoname(1)
except AttributeError:
    raise unittest.SkipTest("if_indextoname not defined")

# Skip test if there is no if_nametoindex()
try:
    socket.if_nametoindex('lo')
except AttributeError:
    raise unittest.SkipTest("if_nametoindex not defined")

# Skip test if there is no SIOCGIFNAME
try:
    socket.SIOCGIFNAME
except AttributeError:
    raise unittest.SkipTest("SIOCGIFNAME not defined")

# Skip test if there is no SIOCGIFINDEX
try:
    socket.SIOCGIFINDEX
except Att
