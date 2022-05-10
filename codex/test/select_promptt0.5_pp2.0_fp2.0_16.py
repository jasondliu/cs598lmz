import select
# Test select.select()
#
# This test is designed to detect a bug in the select() function
# that caused it to return incorrect results for large file
# descriptors.  This bug is present in Python 2.3.3 but not in
# Python 2.3.4.

import os
import select
import socket
import sys
import time
import unittest

from test import test_support

# create a socket pair for use in the test
sock_r, sock_w = socket.socketpair()

