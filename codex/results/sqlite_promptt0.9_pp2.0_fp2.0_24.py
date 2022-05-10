import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') and sqlite3.connect(':memory:',)
# and fails of threading
class TestDirLock(unittest.TestCase):

    daemon = None

    def setUp(self):
        try:
            self.daemon = DirLock(':memory:',)
        except Exception:
            print("skipping directlock")

    @unittest.skip("not valid test here")
    def test_01_init_01(self):
        """
        Initialize lock object and fails inside lock
        """
        with self.assertRaises(Exception):
            self.daemon = DirLock(':memory:',)
            with self.daemon.lock():
                pass
        with self.daemon.lock():
            pass

    @unittest.skip("not valid test here")
    def test_02_init_02(self):
        """
        Forked process inherits lock,
        but thread doesn't prevents access to database
        """

        def _run(task):
            for _ in range(task):
                with self.daemon.
