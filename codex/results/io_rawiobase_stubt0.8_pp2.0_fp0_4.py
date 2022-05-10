import io
class File(io.RawIOBase):
    """
    Class used to handle files.
    """
    def __init__(self, path, mode, access_token):
        """
        Constructor
        :param path: path to file
        :param mode: access mode (r, w, a)
        :param access_token: access token
        """
        self.tkn = access_token
        self.path = path
        self.mode = mode
        if mode[0] == 'r' or mode[1] == 'r':
            self._size = self.size
        else:
            self._size = 0
        self.current_pos = 0

    @property
    def size(self):
        """
        Get size of file
        :return: size of file
        """
        if self.path[0] == '/':
            path = self.path[1:]
        else:
            path = self.path
        dirname, filename = os.path.split(path)
        if dirname[0] == '/':
            dirname = dirname[1:]
        size = 0
        try
