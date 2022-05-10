import bz2
# Test BZ2Decompressor
sample_data = b'BZh91AY&SY.\xc8N\x18\x00\x00\x00\x01\x004\x80P\x00\x00\x00\x00'*500000

bz2_comp = bz2.BZ2Compressor()
data = bz2_comp.compress(sample_data)
data += bz2_comp.flush()
bz2_decomp = bz2.BZ2Decompressor()
decompressed_data = bz2_decomp.decompress(data)
len(decompressed_data)
 
# Another data compression library is the lzma module:
import lzma
# Test LZMACompressor
sample_data = b'This is the sample data to be compressed using LZMA '* 500000

lzma_comp = lzma.LZMACompressor()
data = lzma_comp.compress(sample_data)
data += lzma_comp.flush()
lzma_decomp = lz
