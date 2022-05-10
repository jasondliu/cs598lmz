import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [
        ('a', '@{x(i)}'),
        ('b', '@{x(i)}'),
        ('c', '@{x(i)}'),
    ]

X = ctypes.c_int(5)
S.x = X
S.__str__ = lambda self: "<%s>" % self.x

s = S()

print
print "%r" % s
s.a = 1;  print "%r" % s
s.b = 2;  print "%r" % s
s.c = 3;  print "%r" % s
s.b = 4;  print "%r" % s
s.a = 5;  print "%r" % s
del s.a;  print "%r" % s


print
print "%r" % s
s.a = 1;  print "%r" % s
s.a = 2;  print "%r" % s
s.b = 3;  print "%r" % s
s.c = 4;  print "%r"
