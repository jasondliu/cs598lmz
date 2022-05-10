import io
# Test io.RawIOBase.close()

# io.RawIOBase.close() must exist, even if it does nothing.
# This is a regression test for http://bugs.python.org/issue9376.
class MockRawIO(io.RawIOBase):
    pass

if not hasattr(io.RawIOBase, 'close'):
    raise AssertionError('io.RawIOBase lacks close()')
