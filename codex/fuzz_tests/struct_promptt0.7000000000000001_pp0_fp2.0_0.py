import _struct
# Test _struct.StructData struct.
try:
    from _struct import StructData
except ImportError:
    pass
else:
    # Non-trivial constructor.
    s = StructData(StructType('i'), (1,))
    # Non-trivial attributes.
    s.x = s.y = s.z = 1
    # Non-trivial methods.
    def f(self):
        return self.x + self.y + self.z
    def g(self):
        self.x += 1
        self.y += 1
        self.z += 1
    s.f = f
    s.g = g
    assert s.f() == 3
    s.g()
    assert s.f() == 6
    # Non-trivial getstate/setstate.
    def getstate(self):
        return (self.x, self.y, self.z)
    def setstate(self, state):
        (x, y, z) = state
        self.x = x
        self.y = y
        self.z = z
    s
