import bz2
bz2_file = bz2.BZ2File('compressed_file.bz2', 'w')
bz2_file.write(content)
bz2_file.close()
print(content)
print(bz2_file)

from bz2 import compress
content_compressed = compress('Hello world!')
print(content_compressed)

from bz2 import decompress
content_decompressed = decompress(content_compressed)
print(content_decompressed)

bz2_file_decompressed = bz2.BZ2File('compressed_file.bz2', 'r')
print(bz2_file_decompressed.read())
bz2_file_decompressed.close()

from time import time
from bz2 import compress, decompress

size = 1000
data = ''.join(str(x) for x in range(size))

start = time()
compressed = compress(data)
end = time()
print('compress time: ', end - start)


start = time
