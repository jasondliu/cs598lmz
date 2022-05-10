import select
# Test select.select with a socketpair.
import socket
import sys
import time
import unittest
import warnings
from test import support
if not hasattr(select, 'poll'):
    raise unittest.SkipTest("test needs select.poll")
if not hasattr(select, 'kqueue'):
    raise unittest.SkipTest("test needs select.kqueue")
if not hasattr(select, 'kevent'):
    raise unittest.SkipTest("test needs select.kevent")
if not hasattr(select, 'epoll'):
    raise unittest.SkipTest("test needs select.epoll")
if not hasattr(select, 'devpoll'):
    raise unittest.SkipTest("test needs select.devpoll")
if not hasattr(select, 'select'):
    raise unittest.SkipTest("test needs select.select")
try:
    select.poll()
except select.error:
    raise unittest.SkipTest("test needs functioning select.poll")
try:
    select.kqueue()
except select.error:
    raise un
