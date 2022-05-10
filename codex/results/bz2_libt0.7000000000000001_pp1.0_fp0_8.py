import bz2
bz2.decompress(bz2_data)

import bz2
bz2.compress(data)

from bz2 import BZ2
from io import BytesIO
compressed = BytesIO()
decompressed = BytesIO()
bz2_compressor = BZ2(compressed)
bz2_compressor.write(data)
bz2_compressor.flush()
bz2_decompressor = BZ2(compressed.getvalue())
decompressed.write(bz2_decompressor.read())
bz2_compressor.close()
bz2_decompressor.close()

from cStringIO import StringIO
compressed = StringIO()
decompressed = StringIO()
compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()
compressed.write(compressor.compress(data))
compressed.write(compressor.flush())
decompressed.write(decompressor.decompress(compressed.getvalue()
