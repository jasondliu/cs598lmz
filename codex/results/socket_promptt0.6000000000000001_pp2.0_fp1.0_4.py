import socket
# Test socket.if_indextoname()
import sys
import os
import socket
import unittest
import errno
import select
import struct
import time
import sys
import subprocess
import platform
import random
import string
import select
import signal
import threading
import socket

from test_support import run_unittest, find_unused_port, get_original_stdout

HAVE_SOCKET_IOCTL = hasattr(socket, 'ioctl')

# Filename used for testing
if os.name in ('nt', 'ce'):
    # Use standard place for Win32
    TESTFN = "C:\\socket_test"
elif os.name == 'java':
    # Use standard place for Jython
    TESTFN = "socket_test"
else:
    # Use /tmp for everyone else
    TESTFN = "/tmp/socket_test"

# Save the initial stdout stderr
SAVED_STDOUT = get_original_stdout()
SAVED_STDERR = sys.stderr

# gethostname() often doesn't return the FQDN.
