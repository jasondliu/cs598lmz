import io
class File(io.RawIOBase):
    """
    Raw I/O implementation built upon the read, write and
    fileno system calls.

    :param fd: file descriptor
    """
    def __init__(self, fd): # real signature unknown; restored from __doc__
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """
        :return: this file descriptor
        """
        pass

    def __exit__(self, exc, val, tb): # real signature unknown; restored from __doc__
        """
        Close the file descriptor
        :param exc: exception type, if any
        :param val: exception value
        :param tb: traceback
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        Means the file descriptor will not be used anymore.
        :return:
