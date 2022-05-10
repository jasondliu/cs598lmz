import socket
# Test socket.if_indextoname()
#
# Tested with:
#   Ubuntu 13.10/3.13.0-19-generic/x86_64
#   Ubuntu 13.10/3.11.0-12-generic/i386
#   Mac OS X 10.6.8/10K549/x86_64
#   Mac OS X 10.6.8/10K549/i386

import unittest
import os
import sys
import platform

import test.test_support

from socket import socket, AF_INET, SOCK_DGRAM
from socket import SOL_SOCKET, SO_BROADCAST, SO_BINDTODEVICE
from socket import SO_RCVBUF
import errno


# Ensure select() and poll() support file descriptors > FD_SETSIZE.
test.test_support.requires("poll")

IS_FREEBSD = 'freebsd' in platform.system().lower()

if os.name != 'nt':
    import pwd
    import grp
    getgroups = os.getgroups
    setgroups = os.setgroups

