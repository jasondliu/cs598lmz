import io
# Test io.RawIOBase.write()
import sys

class TestRawIOBase(unittest.TestCase):
    def test_write(self):
        # Issue #5098: the performance of io.RawIOBase.write()
        # was abysmal.
        # Test performance for a simple RawIOBase implementation.
        # This test requires that the write() method of BufferedWriter
        # be fast. On Py2.7, it is currently bested by io.open()
        # on a file opened as buffered binary.

        try:
            io.RawIOBase.write(None)
        except (AttributeError, TypeError):
            # Interpreter with ancient io module
            self.skipTest("insufficiently modern io module")

        # We have to make do with a BufferedWriter instead of a
        # real RawIOBase subclass. The performance observed with
        # io.open(fd=fd) is the same.
        class TestRawIO(io.BufferedWriter):
            def fileno(self):
                return 42
            def isatty(self):
                return False
            def readable
