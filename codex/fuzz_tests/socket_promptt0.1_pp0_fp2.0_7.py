import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno
import socket
import array
import struct
import select
import time
import platform
import subprocess
import re

from test import test_support
from test.test_support import TESTFN, run_unittest, import_module

HOST = test_support.HOST

if sys.platform == 'darwin':
    # On OSX, the default route is not necessarily the first route
    # in the routing table.  This is a problem for the test_route()
    # test.  The following code finds the default route and moves it
    # to the top of the routing table.
    #
    # The code is based on the code in the ifconfig utility.
    SIOCGIFFLAGS = 0xC0206911
    SIOCSIFFLAGS = 0xC0206910
    SIOCGIFADDR = 0xC0206921
    SIOCGIFDSTADDR = 0xC0206931
    SIOCGIFNETMASK = 0xC0206961
    SIOC
