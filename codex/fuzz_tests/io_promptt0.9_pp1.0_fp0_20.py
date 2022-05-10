import io
# Test io.RawIOBase
# The name is misleading: RawIOBase is more like a BufferedIOBase,
# and only suitable for wrapping.  TODO: rename RawIOBase in 3.2.
class FinalizingIO(io.RawIOBase):
    # Read returns nothing, write raises BlockingIOError
    def readable(self):
        return True

    def writable(self):
        return True

    def close(self):
        self.closed = True


def test_raw_close_flushes():
    # Test that RawIOBase.close doesn't raise an exception
    # if it has to flush data
    raw = io.BufferedRWPair(FinalizingIO(), io.BytesIO())
    raw.write(b'1')
    raw.close()


@pytest.mark.skipif(not hasattr(io.RawIOBase, 'fileno'),
                    reason='not supported on this platform')
def test_detach():
    # Detaching twice should be harmless
    r = io.BytesIO(b"asdf")
    if r.detach() is None:
        return 
