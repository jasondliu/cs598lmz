import _struct
# Test _struct.Struct.pack()
(S1,S2,S3) = (_struct.Struct('i'), _struct.Struct('hh'), _struct.Struct('cccc'))
p = S1.pack
print(p(12345678))
p = S1.pack_into
X = bytearray(8)
p(X, 0, 12345678)
print(X)
p(X, 1, 12345678)
print(X)
print(S2.pack(1, 2))
print(S3.pack('a', 'b', 'c', 'd'))
print()
