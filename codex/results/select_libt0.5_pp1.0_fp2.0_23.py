import select
import socket
import sys
import threading
import time
import traceback
import types
import unittest
from test import support
from test.support import threading_helper

# Skip these tests if there is no threading support.
threading_helper.requires_threading(self)

# Test that the module cleans up correctly after a fork
#
# This test is only effective if it's run with a debug build of Python.
# It checks that the module cleans up after a fork, which isn't done
# in a release build.

# Skip this test if the platform doesn't support fork().
support.get_attribute(os, 'fork')

# On Windows, os.fork() doesn't exist, but we can fake it with threading.
if sys.platform == 'win32':
    import _thread
    from _thread import start_new_thread

# Skip this test if the platform doesn't support select().
support.get_attribute(select, 'select')

# Skip this test if the platform doesn't support sockets.
support.get_attribute(socket, 'socket')


