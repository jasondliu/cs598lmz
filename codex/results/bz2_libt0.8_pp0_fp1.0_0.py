import bz2
bz2file = bz2.BZ2File('exemplo2.txt.bz2', 'w')

bz2file.write(data)
bz2file.close()
import bz2
import io

# Use BytesIO to simulate a file opened in binary mode
fake_file = io.BytesIO(data)

decompressor = bz2.BZ2Decompressor()

for block in iter(lambda: fake_file.read(100 * decompressor.decompress_leftover), b''):
    decompressed_data = decompressor.decompress(block)
    if decompressed_data:
        print(decompressed_data)
import bz2
bz2.decompress(data)

import gzip

with gzip.open('exemplo1.txt.gz', 'rb') as s_read:
    for line in s_read:
        print(line)

bytes_data = b'Algumas palavras escritas em bytes.'

with gzip.open('exemplo2.
