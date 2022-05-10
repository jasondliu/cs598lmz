import io
# Test io.RawIOBase as a context manager.
# (Test for SF bug 516062.)
#
#
import io
import unittest


class TestRawIOBase(unittest.TestCase):

    def test_rawiobase_as_context_manager(self):


        class MyRawIO(io.RawIOBase):

            def readable(self):
                return True
            read = lambda self, n: b'x' * n
        f = MyRawIO()
        with f as g:
            self.assertIs(f, g)


if __name__ == '__main__':
    unittest.main()
