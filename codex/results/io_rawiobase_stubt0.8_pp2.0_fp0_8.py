import io
class File(io.RawIOBase):
    """
    Represents a file.
    """
    def __init__(self, fullpath, mode):
        """
        Creates a file wrapper.
        @param fullpath: full path of the file.
        @param mode: file mode.
        """
        self.fullpath = os.path.abspath(fullpath)
        if mode == 'w':
            if os.path.exists(fullpath):
                import warnings
                warnings.warn('Rewriting existing file %s' % fullpath)
            else:
                dirname = os.path.dirname(fullpath)
                if dirname != '' and not os.path.exists(dirname):
                    os.makedirs(dirname)
        self.handle = open(fullpath, mode)

    def close(self):
        """
        Closes the file.  Call this when you're done.
        """
        self.handle.close()

    def read(self, size=-1):
        """
        Reads a chunk of data from the file.
        @param size: how much
