import _struct

class Png:
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'rb')
        self.chunks = []

    def read_chunk(self):
        length = _struct.unpack('>I', self.file.read(4))[0]
        type = self.file.read(4)
        data = self.file.read(length)
        crc = self.file.read(4)
        return {'length': length, 'type': type, 'data': data, 'crc': crc}

    def read_chunks(self):
        while True:
            chunk = self.read_chunk()
            self.chunks.append(chunk)
            if chunk['type'] == 'IEND':
                break

    def get_chunk(self, type):
        for chunk in self.chunks:
            if chunk['type'] == type:
                return chunk
        return None

    def get_chunks(self, type):
        chunks = []
