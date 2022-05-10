import socket
# Test socket.if_indextoname() to get the correct interface name.

import os, sys
import unittest
from test import test_support

# Skip test if AF_PACKET not defined
try:
    socket.AF_PACKET
except AttributeError:
    raise test_support.TestSkipped("socket module has no AF_PACKET constant")

if not hasattr(socket, 'if_indextoname'):
    raise test_support.TestSkipped("socket module has no if_indextoname() method")

