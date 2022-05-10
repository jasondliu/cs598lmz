fn = lambda: None
# Test fn.__code__.co_filename
class TestCodeFilename(unittest.TestCase):
    def test_co_filename(self):
        import sys
        import os
        if hasattr(sys, 'frozen'):
            return # don't run this test for a frozen app
        self.assertTrue(os.path.isabs(fn.__code__.co_filename))
        self.assertTrue(os.path.exists(fn.__code__.co_filename))
        self.assertEqual(fn.__code__.co_filename, __file__)

class TestPystone(unittest.TestCase):
    def test_pystone(self):
        import test.pystone
        self.assertTrue(test.pystone.main() > 0)

class TestReindent(unittest.TestCase):
    def test_reindent(self):
        import tokenize
        from io import StringIO
        src = "if 1:\n  print(12)\n"
        readline = StringIO(src).readline
        tokgen = tokenize.
