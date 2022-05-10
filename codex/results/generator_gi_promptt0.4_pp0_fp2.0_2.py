gi = (i for i in ())
# Test gi.gi_code


class TestGICode(unittest.TestCase):
    def test_gi_code_is_code_object(self):
        self.assertIsInstance(gi.gi_code, types.CodeType)


# Test gi.gi_frame
class TestGIFrame(unittest.TestCase):
    def test_gi_frame_is_none(self):
        self.assertIsNone(gi.gi_frame)


# Test gi.gi_running
class TestGIRunning(unittest.TestCase):
    def test_gi_running_is_false(self):
        self.assertFalse(gi.gi_running)


# Test gi.gi_yieldfrom
class TestGIYieldFrom(unittest.TestCase):
    def test_gi_yieldfrom_is_none(self):
        self.assertIsNone(gi.gi_yieldfrom)


# Test gi.send
class TestSend(unittest.TestCase):
    def test_send_raises_typeerror(self):
        self.
