import bz2
# Test BZ2Decompressor objects
decompressor = bz2.BZ2Decompressor()
with open('data/example4.bz2', 'rb') as input:
    for block in iter(lambda: input.read(100 * decompressor.decompress_block_size), b''):
        output = decompressor.decompress(block)
        if output:
            print(output)

# Test multi-threading
import bz2
import concurrent.futures

class BZ2Compressor:
    def __init__(self):
        self.compressor = bz2.BZ2Compressor()
        self.unused_data = b''

    def compress(self, data):
        result = self.unused_data + data
        self.unused_data = self.compressor.compress(data)
        return result

    def flush(self):
        return self.compressor.flush()

compressor = BZ2Compressor()
with open('lorem.txt', 'rb') as input, \
     open('lorem.txt.bz2',
