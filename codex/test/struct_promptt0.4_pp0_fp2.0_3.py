import _struct
# Test _struct.Struct.pack()

# Test pack with all the standard integer formats

for code in 'bBhHiIlLqQ':
    s = _struct.Struct(code)
    got = s.pack(1)
    expected = code + '\x01'
