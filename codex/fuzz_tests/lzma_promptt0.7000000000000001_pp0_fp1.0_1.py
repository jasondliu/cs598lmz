import lzma
# Test LZMADecompressor.eof
decomp = lzma.LZMADecompressor()
with open('empty_file', 'xb') as f:
    f.write(b'')
with open('empty_file', 'rb') as f:
    assert decomp.eof == False
    decomp.decompress(f.read())
    assert decomp.eof == True

# Test LZMADecompressor.decompress()
# with a file
decomp = lzma.LZMADecompressor()
with open('empty_file', 'rb') as f:
    assert decomp.decompress(f.read()) == b''
    assert decomp.eof == True
with open('empty_file', 'rb') as f:
    assert decomp.decompress(f.read()) == b''

# with a bytes-like object
decomp = lzma.LZMADecompressor()
with open('empty_file', 'rb') as f:
    assert decomp.decompress(f.read()) == b''
    assert decomp.eof == True
