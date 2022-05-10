import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
data = '7zXZ' + 'Y'*5 + 'X'*2 + 'Z'*6
