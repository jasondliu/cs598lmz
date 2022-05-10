import lzma
# Test LZMADecompressor's the states of stream
# state = 0: not started reading
# state = 1: reading
# state = 2: finished reading
# state = -1: error

# Decompress a file with all 0s
data = bytearray(b'\0' * 10)
with lzma.open('testdata/allzeros.xz', 'rb') as f:
    state = f.decompressor.state
    assert state == 0
    f.read(1)
    state = f.decompressor.state
    assert state == 1
    f.read()
    state = f.decompressor.state
    assert state == 2

# Decompress a file with some data
with lzma.open('testdata/empty.xz', 'rb') as f:
    state = f.decompressor.state
    assert state == 0
    f.read(1)
    state = f.decompressor.state
    assert state == 1
    f.read()
    state = f.decompressor.state
    assert state == 2

# Dec
