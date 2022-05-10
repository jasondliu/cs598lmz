import select
# Test select.select(rlist, wlist, xlist[, timeout])
# Test poll.poll(timeout)
# Test poll.poll(timeout) with no events
# Test poll.register(fd[, events])
# Test poll.register(fd[, events]) with unsupported event mask
# Test poll.register(fd[, events]) with an fd twice
# Test poll.unregister(fd)
# Test poll.unregister(fd) with an invalid fd
# Test poll.modify(fd, events)
# Test poll.modify(fd, events) with an invalid fd
# Test poll.modify(fd, events) with an unsupported event mask
# Test poll.poll() in a child process (bpo-25249)

import unittest
import os
import struct
import time
import sys
import errno
import socket
import threading
import multiprocessing
import signal
import subprocess
import traceback
import weakref

import _testcapi

import selectors
import selectors2
from test.support import (import_module, run_unittest,
                         
