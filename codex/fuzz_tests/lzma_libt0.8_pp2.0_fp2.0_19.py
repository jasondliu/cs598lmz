import lzma
lzma.FILTER_X86

from lzma import LZMACompressor, LZMADecompressor
from lzma import FORMAT_ALONE, FORMAT_XZ
from lzma import CHECK_CRC32, CHECK_CRC64, CHECK_SHA256

import shutil

with lzma.open('data.xz', 'rb') as f: 
    file_content = f.read()
    print(file_content) 

with lzma.open('data.xz', 'rt') as f: 
    for line in f:
        print(line) 

with lzma.open('some-images.xz', 'rb') as source, \
     open('images-decompressed', 'wb') as target:
     shutil.copyfileobj(source, target)

compressor = LZMACompressor(format=FORMAT_ALONE,
                            check=CHECK_CRC64, filters=[
                                {"id": lzma.FILTER_LZMA2, "preset":
