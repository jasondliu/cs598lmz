from lzma import LZMADecompressor
LZMADecompressor.flush = zipFileFlush

def readJavaInt(data):
    return struct.unpack('>i', data.read(4))[0]


class NameReader(object):
    def __init__(self, src, stringCount, idCount, nodemap = None):
        self.src = src
        self.stringCount = stringCount
        self.idCount = idCount
        self.stringMap = {}
        self.nodemap = nodemap
    def readNames(self):
        if (self.stringCount + self.idCount == 0) :
            return
        s = self.src.read(self.stringCount * 8)
        for i in range(0, self.stringCount):
            globalOffset = struct.unpack_from(">Q", s, i*8)[0]
            pos = self.src.tell()
            self.src.seek(globalOffset)
            val = self.src.read(2*readJavaInt(self.src))
            try:
                self.src.seek(globalOffset)
                nodeflags
