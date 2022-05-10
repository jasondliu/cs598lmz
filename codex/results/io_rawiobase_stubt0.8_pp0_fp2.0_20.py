import io
class File(io.RawIOBase):
    # Class attributes:
    #   - name -- file name passed to open()
    # Instance attributes:
    #   - mode -- string passed to open(); read/write/append mode
    #             (see io.__init__())
    #   Creating a File checks that the file exists and is a regular file.
    #   This is a thin wrapper over the built-in file type.  It adds
    #   methods to simplify writing a file with the correct name.
    def __init__(self, filename, mode='w+b',
                 encoding=None, errors=None, newline=None):
        self.mode = mode # Store this for use by write_file_if_changed()
        io.RawIOBase.__init__(self)
        self._name = filename
        self._fp = None
        # Set self._fp only after the above is done.  In the case of an
        # exception, it is easiest to close self._fp by using self.close(),
        # which will also quietly ignore any exception.  If the assignments
        # are reversed, a failure in the open()
