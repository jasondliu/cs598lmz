import _struct
# Test _struct.Struct().
s = _struct.Struct('i')
s.size
s.format
s.pack(1)
s.unpack(s.pack(1))
# big endian
s = _struct.Struct('>i')
s.size
s.format
s.pack(1)
s.unpack(s.pack(1))
# alignment requirement
s = _struct.Struct('bBBH')
s.size
s.format
s.pack(1, 1, 1, 1)
s.unpack(s.pack(1, 1, 1, 1))

# Test string formatting.
a = 1
b = (1, 2, 3)
c = []
d = [4, 5]
e = 'abc'
f = ''
g = 'abc\ndef\tg'
h = None
i = {}
j = (1, 'abc')
k = dict(a=1, b=2, c=3)
l = [j]
m = 'ab%scde'
n = [1, 2, 3]
o = 'abcde'
