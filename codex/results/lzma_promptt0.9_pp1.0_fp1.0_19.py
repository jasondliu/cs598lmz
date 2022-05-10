import lzma
# Test LZMADecompressor
s = b'\xf2\x48\xcd\xc9\xc9\x07\x00'

decompressor = lzma.LZMADecompressor()

decompressor.decompress(s)
 

decompressor.unconsumed_tail

decompressor = lzma.LZMADecompressor()

decompressor.decompress(s)

decompressor.unconsumed_tail
 
decompressor = lzma.LZMADecompressor()

decompressor.decompress(s, max_length=100)
decompressor.unconsumed_tail
