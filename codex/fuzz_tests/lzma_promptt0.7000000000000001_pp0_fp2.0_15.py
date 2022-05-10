import lzma
# Test LZMADecompressor
dec = lzma.LZMADecompressor()
data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'
dec.decompress(data)

# Test LZMAFile
f = open('lzma.py', 'rb')
f_lzma = lzma.LZMAFile(f)
f_lzma.read(100)
type(f_lzma)
f_lzma.seek(0, 0)
type(f_lzma)
f_lzma.seek(0, 0)
f_lzma.read(100)
f_lzma.seek(0, 0)
f_lzma.read(100)
f_lzma.tell()
f_lzma.seek(0, 0)
f_lzma.tell()
f_lzma.seek(0, 2)
f_l
