import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno
import platform
import socket
from test import support
from test.support import import_module, run_unittest

ifname_tests = [
    (0, 'lo'),
    (1, 'lo'),
    (2, 'lo'),
    (3, 'lo'),
    (4, 'lo'),
    (5, 'lo'),
    (6, 'lo'),
    (7, 'lo'),
    (8, 'lo'),
    (9, 'lo'),
    (10, 'lo'),
    (11, 'lo'),
    (12, 'lo'),
    (13, 'lo'),
    (14, 'lo'),
    (15, 'lo'),
    (16, 'lo'),
    (17, 'lo'),
    (18, 'lo'),
    (19, 'lo'),
    (20, 'lo'),
    (21, 'lo'),
    (22, 'lo'),
    (23, 'lo'),
    (24, 'lo'),
    (25
