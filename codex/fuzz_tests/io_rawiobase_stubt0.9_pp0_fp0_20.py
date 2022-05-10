import io
class File(io.RawIOBase):
    '''
    Read and write an idiosyncratic binary file format.
    '''
    def __init__(self, file, mode='rb'):
        super().__init__()
        self.name = file
        self.encoding = None
        self.mode = mode
        # Open file and read object count from header.
        self.fh = self._open(file, mode)
        n_objs, = self._read_header(4, b't')
        # Read all objects into memory.
        self.objs = []
        for i in range(n_objs):
            obj_header = self._read_header(8, b'o')
            obj = {
                    'id': obj_header[0],
                    'length': obj_header[1],
                    'data': self.fh.read(obj_header[1])
                    }
            self.objs.append(obj)
        # Create a list of obj ids.
        self.ids = dict(zip(self.objs, range(len(self.objs))))
    def
