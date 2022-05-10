import io
# Test io.RawIOBase
# io.RawIOBase.readinto(b) -> int
# io.RawIOBase.readinto1(b) -> int
# io.RawIOBase.readall() -> bytes
# io.RawIOBase.read() -> bytes
# io.RawIOBase.write(b) -> int
# io.RawIOBase.readable() -> bool
# io.RawIOBase.seekable() -> bool
# io.RawIOBase.writable() -> bool
# io.RawIOBase.seek(offset[, whence]) -> int
# io.RawIOBase.tell() -> int
# io.RawIOBase.truncate([size]) -> int
# io.RawIOBase.close() -> None


class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        with self.assertRaises(NotImplementedError):
            io.RawIOBase().readinto(b'a')

    def test_readinto1(self):
        with self.assertRaises(NotImplementedError):
            io.RawIOBase().read
