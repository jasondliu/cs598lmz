import select
# Test select.select() and select.poll()

import os
import sys
import errno
import unittest
import socket
import subprocess
import threading
import select
import time

tdir = os.path.abspath(os.path.dirname(__file__))
libpath = os.path.join(tdir, '../support')
sys.path.append(libpath)

from support import get_errno

# poll() is not supported on Windows
