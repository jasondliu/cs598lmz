import io
class File(io.RawIOBase):
    """
    This class is a wrapper around the file object returned by the built-in
    open() function. It is necessary to override the default file object
    because the default object does not have a readinto() method.
    """
    def __init__(self, file):
        self.file = file

    def readinto(self, b):
        """
        Read up to len(b) bytes into the writable buffer *b* and return the
        number of bytes read.  If the object is in non-blocking mode and no
        bytes are available, None is returned.
        """
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True
