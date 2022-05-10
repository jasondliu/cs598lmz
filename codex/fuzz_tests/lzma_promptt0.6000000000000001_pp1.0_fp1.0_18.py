import lzma
# Test LZMADecompressor
comp = lzma.LZMADecompressor()
comp.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# Test LZMACompressor
lz = lzma.LZMACompressor()
lz.compress(b'\x00\x00\x00\x00')
# Test LZMAFile
with lzma.open(os.path.join(TESTFN, 'test.xz'), 'wb') as outf:
    outf.write(b'a'*100)
with lzma.open(os.path.join(TESTFN, 'test.xz'), 'rb') as inf:
    if inf.read() != b'a'*100:
        raise TestFailed('Read failed')
with lzma.open(os.path.join(TESTFN
