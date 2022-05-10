from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

import sys
sys.getsizeof(compressed)

sys.getsizeof(original)

# Optimización de memoria
import sys
original = b'This is the original text.'
compressed = lzma.compress(original)
decompressed = lzma.decompress(compressed)

sys.getsizeof(original)

sys.getsizeof(compressed)

sys.getsizeof(decompressed)

# Pickles
import pickle
original = b'This is the original text.'
pickled = pickle.dumps(original)
pickled

len(pickled)

unpickled = pickle.loads(pickled)
unpickled

# Objeto
import lzma
import pickle
class CompressedPickle(object):
    def __init__(self, filename, compressionlevel=9):
        self.filename = filename
        self.compressionlevel = compressionlevel
        try:
            self.fileobj = open(self.filename, 'r+b')
