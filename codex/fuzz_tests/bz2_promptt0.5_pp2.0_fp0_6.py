import bz2
# Test BZ2Decompressor.read()

decomp = bz2.BZ2Decompressor()
assert decomp.read(1) == b'B'
assert decomp.read(1) == b'Z'
assert decomp.read(1) == b'h'
assert decomp.read(1) == b'9'
assert decomp.read(1) == b'1'
assert decomp.read(1) == b'1'
assert decomp.read(1) == b'\x00'
assert decomp.read(1) == b'\x00'
assert decomp.read(1) == b'\x00'
assert decomp.read(1) == b'\x00'
assert decomp.read(1) == b'\x00'
assert decomp.read(1) == b'\x00'
assert decomp.read(1) == b'\x00'
assert decomp.read(1) == b'\x00'
assert decomp.read(1) == b'\x00'
assert decomp.read(1) == b'\x00'
assert decomp.read(1) ==
