import _struct
# Test _struct.Struct
S = _struct.Struct(b'hhl')
with self.assertRaises(TypeError):
    S.pack()
with self.assertRaises(TypeError):
    S.pack(1)
with self.assertRaises(TypeError):
    S.pack(1, 2)
with self.assertRaises(TypeError):
    S.pack(1, 2, 3, 4)

# Test _struct.pack
with self.assertRaises(TypeError):
    _struct.pack()
with self.assertRaises(TypeError):
    _struct.pack(b'hhl')
with self.assertRaises(TypeError):
    _struct.pack(b'hhl', 1)
with self.assertRaises(TypeError):
    _struct.pack(b'hhl', 1, 2)
with self.assertRaises(TypeError):
    _struct.pack(b'hhl', 1, 2, 3, 4)

# Test _struct.unpack
with self.assertRaises(TypeError):
    _struct.unpack()

