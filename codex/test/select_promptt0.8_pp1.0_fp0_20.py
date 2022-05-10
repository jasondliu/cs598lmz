import select
# Test select.select() and select.poll()
# Marc-Andre Lemburg, mal@lemburg.com, 2007-05-22.
#
# Run this through Python's regrtest.py to test its functionality.
# (regrtest.py is part of the standard library)
#
# On Linux, you can use this to test for kernel bugs in the poll()
# system call. To do so, add the option "--test_poll_bug" to the
# command line.
#
# Select is implemented as a thin wrapper around poll(). The poll()
# function is usually a system call, but if there is not enough file
# descriptors available to handle the poll request, it will be
# emulated in Python.
#
# On Windows, there is no poll() system call, and the select.poll()
# object is a dummy which always returns immediately.
#
# The select module is also used in the standard library's asyncore,
# asynchat, socket and httplib modules.

import unittest
import socket
import select
import sys
import time
import os
import tempfile
import err
