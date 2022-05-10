from bz2 import BZ2Decompressor
BZ2Decompressor = BZ2Decompressor


class BZ2File(BinaryIO):
    """代表一个 bz2 文件.
    """

    def __init__(self, name, mode="r", buffering=0, compresslevel=9):
        if mode not in _MODE_CLOSED, _MODE_READ, _MODE_WRITE, _MODE_APPEND:
            raise ValueError(f"invalid mode: {mode!r}")
        if name == "-":
            if mode != _MODE_READ:
                raise ValueError("mode must be 'r' when using stdin")
            binary_file = sys.stdin.buffer
        else:
            binary_file = open(name, mode + "b", buffering)
        self._close = binary_file.close

        if mode in _MODE_READ, _MODE_APPEND:
            self._decompressor = BZ2Decompressor()
            self._buffer = io.BytesIO()
            self._read_size = self._buffer.write(self._decompressor.decompress
