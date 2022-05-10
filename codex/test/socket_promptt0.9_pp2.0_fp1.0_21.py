import socket
# Test socket.if_indextoname support. If this support is missing we need to fake
# up the interface names (ie, find the Linux interface names that match the
# windoze name).
try:
  socket.if_indextoname(1)
  HAVE_IF_INDEXTONAME = 1
except:
  HAVE_IF_INDEXTONAME = 0

import win32con
import win32process
import win32security
import win32event

from xpcom import components, ServerException, COMException, nsError
from xpcom.server.factory import Factory

from xpcom.server.enumerator import SimpleEnumerator

import xpcom.components

from xpcom import components

import os
import signal
import subprocess
import time
import sys

import struct

from IPython.genutils import defaultdict
from IPython.frontend.terminal.interactiveshell import UqEscapes

import traceback

from xpcom._xpcom import GetComponentRegistrar

# This code is borrowed from the xpcom.server.enumerator module
