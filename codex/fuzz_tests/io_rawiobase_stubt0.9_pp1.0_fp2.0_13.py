import io
class File(io.RawIOBase):
    def __init__(self, ip, epn):
        self._ip = ip
        self._epn = epn
        self._buf = io.BytesIO()
        self._pos = 0
        # The following variable is only True if we have read all the data
        # from the server and know that we can't read another byte.
        # We could also use self._ip.peek(1) to see if there are more bytes,
        # but we don't want to block the read operation.

        self._finished = False

    def readable(self):
        return True

    def readinto(self, b):
        if self._finished:
            return 0

        while len(self._buf) / 2 < len(b):
            msg = self._ip.read(self._epn, 1)
            if msg is None:
                self._finished = True
                break
            assert msg.data[0] == 0xA2
            self._buf.write(msg.data[4:len(msg.data) - 1])

        orig_pos = self._buf.tell()
