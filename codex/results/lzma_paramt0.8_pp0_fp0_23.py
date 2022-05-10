from lzma import LZMADecompressor
LZMADecompressor().decompress(df_chunk.iloc[0].comp_mypickle)

print(df_chunk.iloc[0].mypickle)
print(df_chunk.iloc[0].comp_mypickle)

# Custom

pd.compat.pickle_compat.compress(df_chunk.iloc[0].mypickle, compression_level=9)

# zlib

import zlib
compressed = zlib.compress(df_chunk.iloc[0].mypickle, 9)
zlib.decompress(compressed, 31)

# LZMA

from lzma import LZMADecompressor, LZMACompressor

lzma_compressed = LZMACompressor().compress(df_chunk.iloc[0].mypickle)
lzma_compressed += LZMACompressor().flush()
lzma_decompressed = LZMADecompressor().decompress(lzma_compressed)

print(len(l
