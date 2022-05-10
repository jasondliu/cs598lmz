import socket
# Test socket.if_indextoname() and do some other general testing

if socket.has_ipv6:
    AF_INET6 = socket.AF_INET6
    AF_INET = socket.AF_INET
else:
    AF_INET6 = socket.AF_INET
    AF_INET = None

if AF_INET and 'AF_INET6' not in socket.__all__:
    skip("no socket.AF_INET6 on this platform")
    raise skip.SkipTest


from test import support
support.run_unittest(__name__)
support.requires('network')

import errno
import os
import shutil
import signal
import subprocess
import sys
import threading
import time
import unittest
from weakref import proxy
from select import poll, POLLIN
from test.support import run_with_tz
from test.support import TESTFN, captured_stdout, TransientResource, \
                          get_attribute, import_module
from test.script_helper import kill_python, spawn_python
from io import TextIOW
