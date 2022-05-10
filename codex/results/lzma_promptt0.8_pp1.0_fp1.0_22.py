import lzma
# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
lzc.decompress(data)

# Test LZMAFile
f = lzma.LZMAFile(BytesIO(data))
f.read()
f.read()


# +
import bz2 as _bz2
# Test BZ2Decompressor
bz2 = _bz2.BZ2Decompressor()
bz2.decompress(data)

# Test BZ2File
f = _bz2.BZ2File(BytesIO(data))
f.read()
f.read()
# -

import zstd as _zstd
# Test ZstdDecompressor
zstd = _zstd.ZstdDecompressor()
zstd.decompress(data)

# Test ZstdFile
f = _zstd.ZstdFile(BytesIO(data))
f.read()
f.read()

# +
import brotli as _brotli
# Test BrotliDecompressor
brotli = _
