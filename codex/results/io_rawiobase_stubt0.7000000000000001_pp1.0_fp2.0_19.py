import io
class File(io.RawIOBase):
    '''
    File object for reading and writing to a specific file. The file may be
    deleted immediately after being closed.
    '''
    def __init__(self, id, name, path):
        self.id = id
        self.name = name
        self.path = path
        self.closed = False
        self.mode = None
        self.pos = 0
        self.f = None

    def __repr__(self):
        return '<File: {}>'.format(self.path)

    def close(self):
        '''Close the file'''
        if self.closed:
            return
        self.closed = True
        self.mode = None
        self.f = None
        self.pos = 0

    def read(self, sz=-1):
        '''Read data from the file'''
        if self.closed:
            raise ValueError('I/O operation on closed file')
        if not self.mode == 'r':
            raise ValueError('File not open for reading')

        if not self.f:
            self.
