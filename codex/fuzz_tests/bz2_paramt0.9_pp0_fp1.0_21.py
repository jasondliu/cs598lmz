from bz2 import BZ2Decompressor
BZ2Decompressor()
'''

from lzma import LZMADecompressor
from io import BytesIO
from contextlib import closing

with closing(BytesIO(mmy_data)) as src, closing(BytesIO()) as dst:
    decompressor = LZMADecompressor()
    while True:
        buffer = src.read(1024)
        if not buffer:
            break
        data = decompressor.decompress(buffer)
        dst.write(data)
    data = decompressor.flush()
    dst.write(data)
