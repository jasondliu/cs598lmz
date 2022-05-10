from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 2.9.2.2. zlib
import zlib
zlib.decompress(zlib_data)

# 2.9.2.3. lzma
import lzma
lzma.decompress(lzma_data)

# 2.9.2.4. zip
import zipfile
z = zipfile.ZipFile(BytesIO(zip_data))
z.namelist()
z.read('hello.txt')

# 2.9.2.5. gzip
import gzip
with gzip.open(BytesIO(gzip_data), 'rb') as f:
    f.read()

# 2.9.3.1. LZW
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 2.9.3.2. Huffman
import zlib
zlib.decompress(zlib_data)

# 2.9.3.3. Arithmetic
import l
