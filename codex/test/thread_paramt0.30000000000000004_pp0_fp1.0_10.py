import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32m'+__file__+'\x1b[0m\n')).start()

from . import *

class Test_000_000_Basic(unittest.TestCase):
    def test_000_000_basic(self):
        self.assertEqual(1, 1)

class Test_000_001_Basic(unittest.TestCase):
    def test_000_001_basic(self):
        self.assertEqual(1, 1)

class Test_000_002_Basic(unittest.TestCase):
    def test_000_002_basic(self):
        self.assertEqual(1, 1)

class Test_000_003_Basic(unittest.TestCase):
    def test_000_003_basic(self):
        self.assertEqual(1, 1)

