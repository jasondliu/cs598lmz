from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<2cx5si")
s.size

s.unpack(
    b'\x02\x03\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\x02\0\0\0\0\0\0\0'
)

class Struct(Struct):
    def __call__(self, *args):
        return self.pack(*args)

s = Struct("<2cx5si")

s(b'\x02', b'\03', 2)
def func(a, b, c):
    pass

func(1, 2, 3)
func(a = 1, b = 2, c = 3)
func(1, b = 2, c = 3)
def func(a, b, c):
    return a, b, c

func(1, 2, 3)
def func(a, b, c):
    return {'a': a, 'b': b, 'c': c}
