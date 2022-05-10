import bz2
# Test BZ2Decompressor

d = bz2.BZ2Decompressor()
assert d.unused_data == b''

assert b''.join(iter(d.decompress, b'')) == b''
assert d.unused_data == b''

assert b''.join(iter(d.decompress, b'')) == b''
assert d.unused_data == b''

assert d.decompress(DATA) == HELLO
assert d.unused_data == b''

assert b''.join(iter(d.decompress, b'')) == b''
assert d.unused_data == b''

assert d.decompress(DATA, 10) == b''
assert d.unused_data == DATA

decompressed = b''

for i in range(10):
    decompressed += d.decompress(DATA)
    assert d.unused_data == b''

assert decompressed == HELLO + HELLO + HELLO + HELLO + HELLO

assert d.decompress(DATA) == b''
assert d.unused_
