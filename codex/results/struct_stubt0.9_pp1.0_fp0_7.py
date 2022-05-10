from _struct import Struct
s = Struct.__new__(Struct)

def _bf(self, size, endian, tp, name):
	self.fields.append((name, tp, size, endian))
	self._size = (self._size // tp.size) * tp.size + tp.size
	self._cache[name.lower()] = (self._cache.get(name.lower(), 0) + 1, len(self.fields) - 1)

s.f = lambda *a : _bf(s, 8, None, _float, *a)
s.d = lambda *a : _bf(s, 64, None, _double, *a)
s.byte = lambda *a : _bf(s, 8, None, _int, *a)
s.char = lambda *a : _bf(s, 8, None, _char, *a)
s.b = lambda *a : _bf(s, 8, None, _bool, *a)
s.s = lambda *a : _bf(s, 16, None, _short, *a)
s.w = lambda *a : _bf
