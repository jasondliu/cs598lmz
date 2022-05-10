import lzma
# Test LZMADecompressor

from io import BytesIO
from lzma import LZMADecompressor, FORMAT_XZ

decompressor = LZMADecompressor()
source = BytesIO(b'\xfd7zXZ\x00\x00')
decompressor.decompress(source.read())

source.seek(0)
decompressor = LZMADecompressor(format=FORMAT_XZ)
decompressor.decompress(source.read())
# Test LZMADecompressor with multiple calls to decompress

from io import BytesIO
from lzma import LZMADecompressor, FORMAT_XZ

data = b'data' * 1024 * 1024

source = BytesIO(lzma.compress(data))
decompressor = LZMADecompressor(format=FORMAT_XZ)

chunk = source.read(1024)
while chunk:
    decompressor.decompress(chunk)
    chunk = source.read(1024)

