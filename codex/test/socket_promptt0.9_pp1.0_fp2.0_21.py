import socket
# Test socket.if_indextoname and socket.if_indexoname if available.
try:
    socket.if_indextoname(0)
    socket.if_nametoindex('lo')
except AttributeError as e:
    print(e)
    # do not test if these calls are available on this platform
    raise unittest.SkipTest("if_indextoname or if_nametoindex not "
                            "available on this platform")
except OSError as e:
    # test could pass if there are no network interfaces with those indices
    raise unittest.SkipTest('network interface indices unavailable (%s)' % e)

import errno
import io
import os
import platform
import select
import shutil
import signal
import sys
import time
import tempfile
from test import test_support
thread = test_support.import_module('thread')
threading = test_support.import_module('threading')
import unittest
import urllib2

HOST = test_support.HOST
mswindows = (sys.platform == "win32")

# Filename used for
