import io
class File(io.RawIOBase):
    __qualname__ = 'File'

    def __init__(self, file, filename=None, mode='rb', closefd=True, opener=None):
        if isinstance(file, FileIO):
            if filename is None and hasattr(file, '_file'):
                filename = getattr(file, '_file')
            if mode is None and hasattr(file, '_mode'):
                mode = getattr(file, '_mode')
            if closefd is None and hasattr(file, '_closefd'):
                closefd = getattr(file, '_closefd')
        fd = None
        if isinstance(file, int):
            (fd, mode, closefd) = (file, filename, mode)
            if filename is not None:
                if isinstance(filename, str):
                    file = open(filename, mode, closefd=closefd, opener=opener)
                elif hasattr(filename, 'read') or hasattr(filename, 'write'):
                    file = filename
                else:
                    raise TypeError('invalid file
