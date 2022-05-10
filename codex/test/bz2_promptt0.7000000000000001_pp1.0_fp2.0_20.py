import bz2
# Test BZ2Decompressor class

class BZ2DecompressReader:

    def __init__(self, stream, max_size=0, block_size=1024):
        self.stream = stream
        self.max_size = max_size
        self.block_size = block_size
        self.decompressor = bz2.BZ2Decompressor()

    def read(self):
        data = b''
        while True:
            block = self.stream.read(self.block_size)
            data += self.decompressor.decompress(block)
            if self.decompressor.eof:
                break

            if self.max_size > 0 and len(data) > self.max_size:
                break

            if len(block) < self.block_size:
                break

        return data

def get_read_size(size):
    return min(size, 1024)

def iter_bz2_data(stream, block_size=1):
    data = []
    decompressor = bz2.BZ2Decompressor()
   
