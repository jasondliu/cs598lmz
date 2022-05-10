import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

class C(PyCapsule):

    def __init__(self):
        PyCapsule.__init__(self, S)

    def __getattr__(self, name):
        return getattr(self.capsule, name)

    def __setattr__(self, name, value):
        if name == "capsule":
            self.__dict__[name] = value
        else:
            setattr(self.capsule, name, value)

s = C()

s.x = 1.1
s.y = 3.3
print(s.x)
print(s.y)
</code>

