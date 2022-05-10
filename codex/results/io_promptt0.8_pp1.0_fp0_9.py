import io
# Test io.RawIOBase for compatibility (e.g. Python 2.6)
if not isinstance(io.RawIOBase, type):
    class io:
        @staticmethod
        def RawIOBase():
            pass


def extend_bytes(b, n):
    try:
        return b + b'\0' * (n - len(b))
    except TypeError:
        # b not a bytes object
        return b.to_bytes(n, 'big') + b'\0' * (n - len(b.to_bytes(n, 'big')))


class _BaseSerial(io.RawIOBase):
    """
    Base class for serial communication.
    """
    def __init__(self, port, baudrate, timeout=None, write_timeout=None,
                 rtscts=False, xonxoff=False, dsrdtr=False, inter_byte_timeout=None,
                 exclusive=False):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.write_timeout = write_
