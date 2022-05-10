import lzma
# Test LZMADecompressor

from io import BytesIO
from lzma import LZMADecompressor

compressed = BytesIO()
decompressor = LZMADecompressor()
decompressor.decompress(compressed.read())

# Test LZMADecompressor.flush

from io import BytesIO
from lzma import LZMADecompressor

compressed = BytesIO()
decompressor = LZMADecompressor()
decompressor.decompress(compressed.read())
decompressor.flush()

# Test LZMADecompressor.copy

from io import BytesIO
from lzma import LZMADecompressor

compressed = BytesIO()
decompressor = LZMADecompressor()
decompressor.decompress(compressed.read())
decompressor.copy()
