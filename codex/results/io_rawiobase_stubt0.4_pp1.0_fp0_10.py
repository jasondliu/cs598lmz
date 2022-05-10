import io
class File(io.RawIOBase):
    """
    File object

    :param path: path to the file
    :param mode: file opening mode
    :param encoding: encoding
    :param errors: error handling scheme
    :param newline: newline
    :param closefd: close file descriptor
    :param opener: custom opener
    """

    def __init__(self, path, mode='r', encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self._path = path
        self._mode = mode
        self._encoding = encoding
        self._errors = errors
        self._newline = newline
        self._closefd = closefd
        self._opener = opener

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __repr__(self):
        return 'File({}, {}, {}, {}, {}, {})'.format(
            self._path,
            self._mode,
            self._encoding,
           
