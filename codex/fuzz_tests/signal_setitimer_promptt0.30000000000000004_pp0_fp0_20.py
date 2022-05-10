import signal
# Test signal.setitimer()
#
# This test is not part of the standard test suite, because it requires
# superuser privileges to run.
#
# This test is a bit tricky to run, because it needs to be run as root.
#
# You can run it like this:
#
#   sudo python test_signal.py setitimer
#
# If you get errors like "IOError: [Errno 13] Permission denied", you
# probably need to add the following line to /etc/sudoers:
#
#   Defaults !requiretty
#
# This test is also tricky to write, because it needs to run in a
# subprocess, because it needs to call os.setuid() to drop privileges
# after calling os.setuid(0) to gain superuser privileges.
#
# This test is also tricky to write, because it needs to run in a
# subprocess, because it needs to call os.setuid() to drop privileges
# after calling os.setuid(0) to gain superuser privileges.

import os
import sys
import time
import unittest
from test import test_support
