import socket
# Test socket.if_indextoname
#

import os
import sys
import unittest
import socket
import subprocess

from test.support import (
    run_unittest, run_subprocess, find_unused_port,
    import_module, cpython_only)
from test.support.script_helper import assert_python_ok

import_module('fcntl')

HAVE_NETWORK = True
try:
    socket.create_connection(('www.python.org', 80))
except OSError:
    HAVE_NETWORK = False

HOST = '127.0.0.1'
HOSTv6 = '::1'
PORT = find_unused_port()

# Get a list of all interface names.
interface_names = socket.if_nameindex()
interface_names = [i[1] for i in interface_names]

# Get a list of all up interface names.
up_interface_names = []
for interface_name in interface_names:
    if_flags = socket.if_flags(interface_name)
    if if_
