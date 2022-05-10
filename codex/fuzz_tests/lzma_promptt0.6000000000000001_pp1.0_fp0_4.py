import lzma
# Test LZMADecompressor
l = lzma.LZMADecompressor()
l.decompress(b'\x00\x00\x00\x00')

# Test LZMACompressor
l = lzma.LZMACompressor()
l.compress(b'\x00\x00\x00\x00')

# Test LZMAFile
with lzma.LZMAFile(io.BytesIO(b'')) as f:
    f.read()
    f.read(10)
    f.read1(10)
with lzma.LZMAFile(io.BytesIO(b''), mode='w') as f:
    f.write(b'')
with lzma.LZMAFile(io.BytesIO(b''), mode='r') as f:
    f.seek(0, 0)
    f.tell()
    f.readinto(bytearray(10))
    f.seek(0, 0)
    f.seek(0, 1)
    f.seek(0, 2)
   
