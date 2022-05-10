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
if hasattr(select, 'poll'):
    class SelectPollTest(unittest.TestCase):
        def setUp(self):
            self.p = subprocess.Popen([sys.executable,
                                       '-c',
                                       'import socket,time;'
                                       's=socket.socket(socket.AF_INET,'
                                       'socket.SOCK_STREAM);'
                                       's.bind(("127.0.0.1",0));'
                                       's.listen(1);'
                                       'print(s.getsockname()[1]);'

