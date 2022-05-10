import io
# Test io.RawIOBase closing behavior.


class TestRawIOBaseClosing(unittest.TestCase):
    # Issue 9109: io.RawIOBase.close() should not raise an exception
    # if self.close() was already called.

    def test_close(self):
        class MockRawIO(io.RawIOBase):

            def close(self):
                pass
        m = MockRawIO()
        m.close()
        m.close()


def test_context_manager():
    io.IOBase()
    with io.RawIOBase() as b1:
        pass
    with io.BufferedIOBase() as b2:
        pass
    with io.TextIOBase() as b3:
        pass
    io.IOBase.close()
    io.RawIOBase.close()
    io.BufferedIOBase.close()
    io.TextIOBase.close()


if __name__ == '__main__':
    unittest.main()
