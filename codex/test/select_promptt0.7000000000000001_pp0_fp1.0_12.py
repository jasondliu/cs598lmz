import select
# Test select.select() and select.poll() with a large number of
# file descriptors.  (Tested with Linux 2.4.18, glibc 2.2.5.)

import os
import select
import socket
import sys

# How many file descriptors to test with.
try:
    num_fds = int(sys.argv[1])
except (IndexError, ValueError):
    num_fds = 50000

