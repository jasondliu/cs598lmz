import socket
# Test socket.if_indextoname
#
# In this testcase, we create a bunch of virtual interfaces for testing.
# We also call if_indextoname to fetch their names and compare them to
# the names we expect.
#
# Based on testcase by Dan Williams <dcbw@redhat.com>

import os
import signal
import socket
import sys
import time

from avocado import main
from avocado.utils import process

VIRTUAL_IFACE_PREFIX = "test"
TEST_IFACES = 10
TIMEOUT = 60


def setup():
    if os.geteuid() != 0:
        return 'Must be root'


def test():
    # Setup and get the names of the virtual interfaces
    test_iface_names = []
