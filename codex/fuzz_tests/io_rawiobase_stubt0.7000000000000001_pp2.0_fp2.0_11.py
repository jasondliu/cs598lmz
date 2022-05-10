import io
class File(io.RawIOBase):
    def __init__(self, file_path=None, file_id=None, url=None, chunk_size=1024, mode='r'):
        super(File, self).__init__()
        self.file_path = file_path
        self.url = url
        self.file_id = file_id
        self.chunk_size = chunk_size
        self.mode = mode
        self.cursor = 0
        self.length = 0

        if self.file_id is not None:
            response = get(self.file_id)
            if response.status_code == 200:
                self.response = response
                self.length = int(response.headers.get('Content-Length', 0))
            else:
                raise Exception('No such file with id %s' % self.file_id)

        elif self.file_path is not None:
            with open(self.file_path, 'rb') as f:
                self.file_id = upload(f)['_id']
                self.response = get(self.file_id
