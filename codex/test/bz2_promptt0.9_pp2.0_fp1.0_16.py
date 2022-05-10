import bz2
# Test BZ2Decompressor
from io import BytesIO

uncompressed_data = b'abcabcabcabcabcabc' * 10 * 1024 * 1024

class BytesIOOutput:
    def __init__(self):
        self.buffer = BytesIO()
        self.compressor = bz2.BZ2Compressor()

    def write(self, block):
        self.buffer.write(self.compressor.compress(block))

    def flush(self):
        self.buffer.write(self.compressor.flush())
        self.buffer.seek(0)

#for line in fileinput.input():
#    compressed_data = line

decompressed_data = b''
