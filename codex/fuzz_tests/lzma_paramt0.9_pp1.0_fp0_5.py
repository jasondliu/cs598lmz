from lzma import LZMADecompressor
LZMADecompressor.decompress(LZMADecompressor.decompress(data))

# Substituting decompression
from zlib import decompressobj
decompressobj().decompress(decompressobj().decompress(data))

# Or use a transfrom to do it in one line
from zlib import decompress, MAX_WBITS
from io import BytesIO
decompress(BytesIO(decompress(BytesIO(data).getvalue(), -MAX_WBITS)), -MAX_WBITS)
</code>

