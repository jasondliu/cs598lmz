import lzma
# Test LZMADecompressor
#with open('/tmp/test.lzma', 'rb') as f:
#    decomp = lzma.LZMADecompressor()
#    data = decomp.decompress(f.read())
#    print(data)

# Test LZMACompressor
#with open('/tmp/test.lzma', 'wb') as f:
#    comp = lzma.LZMACompressor()
#    compdata = comp.compress(b'Hello, World!')
#    compdata += comp.flush()
#    f.write(compdata)

# Test LZMAFile
#with lzma.open('/tmp/test.lzma', 'rb') as f:
#    print(f.read())

# Test LZMAFile
#with lzma.open('/tmp/test.lzma', 'wb') as f:
#    f.write(b'Hello, World!')

# Test LZMAFile with filters
#filters = [
#    dict(id=lzma.FIL
