from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

#%%
# bz2
import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)
decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

#%%
# bz2
import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressor = bz2.BZ2Compressor()
compressed1 = compressor.compress(original_data)
compressed2 = compressor.compress(original_data)
compressed3 = compressor.flush()
print('Compressed   :', len(compressed1), compressed1)
print('Compressed   :', len(compressed2), compressed2)
print('Compressed   :', len(compressed
