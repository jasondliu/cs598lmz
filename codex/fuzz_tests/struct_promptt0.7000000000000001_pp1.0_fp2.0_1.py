import _struct
# Test _struct.Struct
b = _struct.Struct('b')
c = _struct.Struct('c')
h = _struct.Struct('h')
i = _struct.Struct('i')
l = _struct.Struct('l')
q = _struct.Struct('q')
B = _struct.Struct('B')
H = _struct.Struct('H')
I = _struct.Struct('I')
L = _struct.Struct('L')
Q = _struct.Struct('Q')
f = _struct.Struct('f')
d = _struct.Struct('d')
s = _struct.Struct('s')
p = _struct.Struct('p')
P = _struct.Struct('P')
x = _struct.Struct('x')
X = _struct.Struct('X')

# Test _struct.pack
def test_pack(self):
    eq = self.assertEqual
    struct = _struct.pack
    self.assertRaises(TypeError, struct, 'x')
    self.assertRaises(TypeError, struct, 'c', 'c')
    self.assertRaises(
