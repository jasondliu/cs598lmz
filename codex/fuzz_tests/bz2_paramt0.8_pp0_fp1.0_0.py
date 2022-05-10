from bz2 import BZ2Decompressor
BZ2Decompressor()

# check if next_byte() returns correct value, pos, and remaining
d = BZ2Decompressor()
for i in range(100):
    d.decompress(b'\x42\x5a')
assert d.next_byte() == 0x42, "next_byte() returns incorrect value"
assert d.next_byte() == 0x68, "next_byte() returns incorrect value"
assert d.next_byte() == 0x0, "next_byte() returns incorrect value"
d.decompress(b'\x42\x5a')
assert d.next_byte() == 0x42, "next_byte() returns incorrect value"
try:
    d.decompress(b'\x42\x5a')
except EOFError:
    pass
assert d.next_byte() == 0x0, "next_byte() returns incorrect value"

# check if next_char() returns correct value, pos, and remaining
d = BZ2Decompressor()
for i in range(100):
    d.decompress(b'
