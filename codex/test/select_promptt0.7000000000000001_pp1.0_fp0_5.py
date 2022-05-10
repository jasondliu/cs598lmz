import select
# Test select.select(), select.poll(), and select.epoll().
#
# This test does not do anything to guarantee that the object being
# used is the correct object.  For example, if we call a method on the
# epoll object that is not supported on this platform, the test
# does nothing to detect that.
#
# This test does not do anything to guarantee that the object being
# used is the correct object.  For example, if we call a method on the
# epoll object that is not supported on this platform, the test
# does nothing to detect that.
#
# This test does not do anything to guarantee that the object being
# used is the correct object.  For example, if we call a method on the
# epoll object that is not supported on this platform, the test
# does nothing to detect that.
import socket
import os
import stat
import fcntl
import sys
import errno
import atexit
import signal
import unittest
import asyncore
import asynchat
import subprocess
import struct
import time
import threading
import tempfile
import weakref
import selectors
