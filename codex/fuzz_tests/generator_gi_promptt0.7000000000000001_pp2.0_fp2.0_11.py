gi = (i for i in ())
# Test gi.gi_code is NULL
class TestCodeNull(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(gi.gi_code)

# Test gi.gi_frame is NULL
class TestFrameNull(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(gi.gi_frame)

# Test gi.gi_running
class TestRunning(unittest.TestCase):
    def test_false(self):
        self.assertFalse(gi.gi_running)

# Test gi.gi_yieldfrom
class TestYieldFrom(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(gi.gi_yieldfrom)

# Test gi.gi_weakreflist
class TestWeakRefList(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(gi.gi_weakreflist)

# Test gi.__name__
class TestName(unittest.TestCase
