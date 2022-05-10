import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import os

class _TestThread(threading.Thread):
    def __init__(self, test_case, thread_id, conn):
        super(_TestThread, self).__init__()
        self.test_case = test_case
        self.thread_id = thread_id
        self.conn = conn

    def run(self):
        c = self.conn.cursor()
        c.execute('PRAGMA cache_size=-%d' % (1024 * self.thread_id))
        c.execute('PRAGMA page_size=%d' % (512 * self.thread_id))

        self.test_case.assertEqual(c.fetchone(), (512 * self.thread_id,))

        # Test that the settings are thread-local.
        c2 = self.conn.cursor()
        c2.execute('PRAGMA cache_size')
        self.test_case.assertEqual(c2.fetchone(), (100,))
        c2
