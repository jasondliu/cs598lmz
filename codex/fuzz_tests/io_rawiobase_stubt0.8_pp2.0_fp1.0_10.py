import io
class File(io.RawIOBase):
    """
    This class is used to store and query a file in netfs
    """
    def __init__(self, client, name, size, is_dir=False, rev=0, parent=None):
        super().__init__()
        self.client = client
        self.name = name
        self.size = size
        self.is_dir = is_dir
        self.rev = rev
        self.parent = parent
        self.__offset = 0
        self.__read_offset = 0
        self.__fread_offset = 0
        self.__fwrite_offset = 0
        self.__size = 0
        self.__cache_size = 0
        self._updatetime = time.time()
        self.__cache = {}
        self.headers = {}

    def _stat(self):
        request_body = {}
        if self.parent is None:
            request_body['path'] = self.name
        else:
            request_body['path'] = self.parent / self.name
        request_body['list'] = False

