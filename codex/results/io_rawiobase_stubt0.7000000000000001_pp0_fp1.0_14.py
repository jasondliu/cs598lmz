import io
class File(io.RawIOBase):
    '''
    Wrapper around open() to provide a file-like interface.

    Instances of this class will always be context managers, so
    they can be used in with statements.

    >>> with File('/etc/passwd') as f:
    ...     print('File is open')
    >>> print('File is closed')
    '''

    def __init__(self, *args, **kwargs):
        self._open_args = args
        self._open_kwargs = kwargs
        self._f = None

    def __enter__(self):
        self._f = open(*self._open_args, **self._open_kwargs)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._f.close()

    def read(self, n=-1):
        return self._f.read(n)

    def seek(self, offset, whence=io.SEEK_SET):
        return self._f.seek(offset, whence)

    def readinto(self, b):
        return self._
