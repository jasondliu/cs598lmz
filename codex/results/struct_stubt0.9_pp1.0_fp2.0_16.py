from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('cb?ehl', 0)
s.pack(1, 2, 3)

class Struct(Struct):
    def pack(self, *args):
        return "pack(%s)" % ", ".join(map(str, args))

s = Struct.__new__(Struct)
s.__init__('cb?ehl', 0)
s.pack(1, 2, 3)

class Struct(Struct):
    def __call__(self, v1, v2, v3):
        return "call(%s, %s, %s)" % (v1, v2, v3)

s = Struct.__new__(Struct)
s.__init__('cb?ehl', 0)
s.pack(1, 2, 3)
s(1, 2, 3)

# function objects
def f():
    return "f()"

f.__call__ = None
f()

def f():
    print("f()")

f.__call__ = None
f()

def g():
   
