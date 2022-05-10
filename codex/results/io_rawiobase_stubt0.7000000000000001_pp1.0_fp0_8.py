import io
class File(io.RawIOBase):
    """File(name: str, mode: str = 'r', buffering: int = -1, encoding: str = None, errors: str = None, newline: str = None, closefd: bool = True, opener: Any = None)"""
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        pass

    @classmethod
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def __new__(cls, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None): # reliably restored by inspect
        # no doc
        pass

    __qualname__ = 'File'


class Flock(object):
    """
    Flock(fd, op: int)
    
    A wrapper around the f
