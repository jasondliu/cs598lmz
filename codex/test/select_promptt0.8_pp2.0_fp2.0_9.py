import select
# Test select.select
import socket
# Test select.poll
import subprocess
# Test select.epoll
import sys
# Test select.poll
import test.support
import time
import threading
import unittest
import warnings

try:
    import msvcrt
except ImportError:
    # Test cannot run without msvcrt.GetStdHandle.
    pass

# Use select.poll on Windows and select.epoll on Linux.
if hasattr(select, "poll"):
    poll_func = select.poll
else:
    poll_func = select.epoll

# Use select.epoll on Linux.
if hasattr(select, "epoll"):
    epoll_func = select.epoll
else:
    epoll_func = None

# Use select.kqueue on BSDs.
if hasattr(select, "kqueue"):
    kqueue_func = select.kqueue
else:
    kqueue_func = None

# Use select.devpoll on Solaris.
if hasattr(select, "devpoll"):
    devpoll
