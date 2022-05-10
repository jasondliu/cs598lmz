import io
class File(io.RawIOBase):
    """
    An open file.

    A proxy for `open()` that can be used in `with` statements.

    Parameters
    ----------
    name : str, optional
        The file name.
    mode : str, optional
        The mode for `open()`.
    """
    def __init__(self, name=None, mode='r'):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, *args):
        self.file.close()
        return False


class Writer(io.RawIOBase):
    """
    Proxy to `:class:File` to write to it.

    Parameters
    ----------
    name : str, optional
        The file name.
    mode : str, optional
        The mode for `open()`.
    """
    def __init__(self, name=None, mode='w'):
        super().__init__()
        self.file = File(
