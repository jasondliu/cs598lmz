import lzma
lzma.decompress(lzma.compress(data))

#%%
import bz2
bz2.decompress(bz2.compress(data))

#%%
import zlib
zlib.decompress(zlib.compress(data))


#%%
import zlib
import bz2
import lzma

original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)

compressed = zlib.compress(original_data)
print('Compressed   :', len(compressed), compressed)

decompressed = zlib.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

print()

compressor = bz2.BZ2Compressor()
compressed = compressor.compress(original_data)
compressed += compressor.flush()
print('Compressed   :', len(compressed), compressed)

decompressor = bz2.BZ2Decompressor()
decompressed =
