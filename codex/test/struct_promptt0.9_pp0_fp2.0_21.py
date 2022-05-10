import _struct
# Test _struct.Struct.pack()
assert _struct.Struct('@i').pack(-1) == rpbc.Struct('@i').pack(-1)

# Test _struct.Struct.unpack()
assert rpbc.Struct('@i').unpack(_struct.Struct('@i').pack(-1)) == [-1]

# Test _struct.Struct.calcsize()
assert (rpbc.Struct('@i').size == _struct.Struct('@i').calcsize())

# Test _struct.pack()
assert _struct.pack('@i', -1) == rpbc.pack('@i', -1)

# Test _struct.unpack()
assert rpbc.unpack('@i', _struct.pack('@i', -1)) == [-1]

# Test _struct.calcsize()
assert rpbc.size('@i') == _struct.calcsize('@i')
