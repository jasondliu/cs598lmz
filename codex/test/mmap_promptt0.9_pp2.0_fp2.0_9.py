import mmap
# Test mmap.mmap class with context manager.
with mmap.mmap(-1, 10) as m:
    pass

# Test bytearray.fromhex()
ba = bytearray(b'abcd')
ba.fromhex('abcdef')
print(ba)  # b'abcdef'

# Test bytearray.hex()
ba = bytearray(b'abcd')
print(ba.hex())  # 61626364

# Test __setitem__
ba = bytearray(b'abcd')
ba[0:3] = bytearray(b'123')
print(ba)  # b'123d'

# Test 's*' in struct
import struct
print(struct.unpack('ss*s', b'abcabcabcabcabcabcabcabcabcabc'))

# Test pickle protocol 2
import pickle

class C():
    def __init__(self):
        self.att = 'aa'

c = C()
