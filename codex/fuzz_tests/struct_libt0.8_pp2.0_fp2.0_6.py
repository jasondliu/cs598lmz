import _struct

class Unpacker:
    def __init__(self, file):

        self.file = file

        self.header = {
            'tile': [],
            'chunk': [],
            'code': [],
            'name': [],
            'desc': [],
        }

        self.tiles = []
        self.chunks = []
        self.codes = []
        self.names = []
        self.descs = []

        self.readFile()

    def readFile(self):
        self.file.seek(0, 0)
        self.header['tile'] = _struct.unpack('<8sI', self.file.read(12))
        self.header['chunk'] = _struct.unpack('<8sI', self.file.read(12))
        self.header['code'] = _struct.unpack('<8sI', self.file.read(12))
        self.header['name'] = _struct.unpack('<8sI', self.file.read(12))
        self.header['
