import ctypes

class S(ctypes.Structure):
    x = 0
    
    @property
    def y(self):
        return self.x
    @y.setter
    def y(self, value):
        self.x = value

s = S()
assert s.y == 0
s.y = 42
assert s.y == 42

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    
    @property
    def y(self):
        return self.x
    @y.setter
    def y(self, value):
        self.x = value

s = S()
assert s.y == 0
s.y = 42
assert s.y == 42

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    
    @property
    def y(self):
        return self.x

s = S()
assert s.y == 0
s.y = 42
assert s.y == 42

class S(ctypes.Structure):
    _fields_ =
