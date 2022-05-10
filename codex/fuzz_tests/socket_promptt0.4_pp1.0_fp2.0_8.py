import socket
# Test socket.if_indextoname

import unittest
import os
import sys
import errno
import platform
import time
import select
import struct
import subprocess
import re

from test import support
from test.support import import_module

HOST = support.HOST

def if_indextoname(ind):
    """
    Return the name of the interface corresponding to the given index.
    """
    if not hasattr(socket, "if_indextoname"):
        raise unittest.SkipTest("if_indextoname not implemented")
    return socket.if_indextoname(ind)

def if_nametoindex(name):
    """
    Return the index of the interface corresponding to the given name.
    """
    if not hasattr(socket, "if_nametoindex"):
        raise unittest.SkipTest("if_nametoindex not implemented")
    return socket.if_nametoindex(name)

def get_if_indextoname_interface_list():
    """
    Return a list of all the interfaces on the system.
   
