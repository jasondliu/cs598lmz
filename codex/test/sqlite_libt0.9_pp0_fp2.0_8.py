import ctypes
import ctypes.util
import threading
import sqlite3

from gevent import sleep
from gevent.core import loop
from gevent.core import assert_switches
from gevent.event import Event
from gevent.fileobject import FileObjectThread
from gevent.pool import Group

from test import test_support

try:
    from gevent.select import kqueue, kevent
except ImportError:
    pass


class TestCase(TestCase):

    switch_expected = True

    # POSIX only
    def test_get_write_buffer_size(self):
        fobj = FileObjectThread(12345)
        # size of actual buffer *cannot* be verified without
        # too much pain.  However, the methods should return 0
        # when the object is closed.
        fobj.close()
        self.assertEqual(fobj.get_write_buffer_size(), 0)
        self.assertEqual(fobj.get_write_buffer_capacity(), 0)

