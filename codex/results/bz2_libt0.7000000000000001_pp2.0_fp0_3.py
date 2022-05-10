import bz2
bz2_comp = bz2.BZ2Compressor()
next(bz2_comp)

bz2_comp.compress(b'Hello')

bz2_comp.flush()

# Filters
# Compression
from io import BytesIO
import zlib
compressor = zlib.compressobj(9)

buf = BytesIO()

buf.write(compressor.compress(b'Hello'))
buf.write(compressor.compress(b' '))
buf.write(compressor.compress(b'World'))
buf.write(compressor.flush())

buf = BytesIO()
buf.write(compressor.compress(b'Hello'))
buf.write(compressor.compress(b' '))
buf.write(compressor.compress(b'World'))
buf.write(compressor.flush())

buf.getvalue()

# Decompression
decompressor = zlib.decompressobj()

buf = BytesIO()

buf.write(decompressor.
