import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.TextIOBase

print('Test io.TextIOBase')

class TestIOTextIOBase(unittest.TestCase):
    def test_read(self):
        class TestIOTextIOBaseRead(io.TextIOBase):
            def read(self, size=-1):
                return "Hello world!"
        self.assertEqual(TestIOTextIOBaseRead().read(), "Hello world!")
        self.assertEqual(TestIOTextIOBaseRead().read(2), "He")
        self.assertEqual(TestIOTextIOBaseRead().read(100), "Hello world!")

    def test_readline(self):
        class TestIOTextIOBaseReadLine(io.TextIOBase):
            def readline(self):
                return "Hello world!"
        self.assertEqual(TestIOTextIOBaseReadLine().readline(), "Hello world!")

    def test_readlines(self):
        class TestIOTextIOBaseReadLines(io.TextIO
