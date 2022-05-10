import _struct
# Test _struct.Struct

s = _struct.Struct("I 2s f")
print(s.size, s.format)
print(s.pack(1, b"spam", 2.3))
print(s.unpack(b'\x01spam\x00\x00\x80?'))

print(type(s.format))

try:
    s.pack()
except TypeError:
    print("TypeError")
try:
    s.pack(1, 2)
except TypeError:
    print("TypeError")
try:
    s.unpack(b"12345")
except TypeError:
    print("TypeError")
try:
    s.unpack(b"12345", b"67890")
except TypeError:
    print("TypeError")

# Test _struct.pack.
