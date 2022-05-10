from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# example 2
from bz2 import BZ2File
f = BZ2File('sample.bz2', 'w')
f.write('hello world! this is just a sample text')
f.close()

f = BZ2File('sample.bz2', 'r')
f.read()
f.close()

# example 3
import bz2
data = b'This is the original text.'
compressed = bz2.compress(data)
decompressed = bz2.decompress(compressed)
decompressed == data
# True
