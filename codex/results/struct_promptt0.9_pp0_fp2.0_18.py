import _struct
# Test _struct.Struct('i')
print (_struct.Struct('i')(123))	# test default endianness
print (_struct.Struct('>i')(123))
print (_struct.Struct('<i')(123))

# Test _struct.pack()
t1 = (_struct.Struct('i'), 123)
t2 = (_struct.Struct('>i'), 123)
t3 = (_struct.Struct('<i'), 123)
print (_struct.pack(*t1))
print (_struct.pack(*t2))
print (_struct.pack(*t3))

# Test _struct.unpack()
s1 = _struct.pack(*t1)
s2 = _struct.pack(*t2)
s3 = _struct.pack(*t3)
print (_struct.unpack(*t1 + (s1,)))
print (_struct.unpack(*t2 + (s2,)))
print (_struct.unpack(*t3 + (s3,)))

# More tests
try:
    t4 = (_struct.Struct('i'), 123, 124)
    print (_struct.pack(*t4
