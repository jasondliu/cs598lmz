from _struct import Struct
s = Struct.__new__(Struct)
s.formatstring = '!BBB'
s.size = 3
s.pack = s.__call__
s.unpack = s.unpack_from
s.calcsize = s.size

class Buffer(object):
    def __init__(self, data=None, offset=0):
        self.data = data or ''
        self.offset = offset
    def get(self, size):
        data = self.data[self.offset:self.offset+size]
        self.offset += size
        return data
    def put(self, data):
        self.data += data
    def gets(self):
        data = self.data[self.offset:]
        self.offset = len(self.data)
        return data
    def puts(self, data):
        self.data += data
    def get_be(self, size):
        return self.get(size).encode('hex')[::-1]
    def get_le(self, size):
        return self.get(size).encode('hex')
    def get_u
