import ctypes
ctypes.cast(ctypes.addressof(a), ctypes.POINTER(ctypes.c_int)).contents.value
ctypes.addressof(a)

a.contents.value
a.contents
a

type(a)
# isinstance(a, bool)
# bool(a)

a.contents.value
a.value

b = S([1,2,3])

a.contents = b
a.contents
a.contents = None
a.contents
a.contents = b
a.contents
b.value
b
# b[0]

b.contents = pointer(b)
b.contents

b.contents.contents
b.contents.contents.contents.contents
# .contents 
# .contents.contents.contents.contents


p = pointer(1)
p.contents
p.contents.value
p.contents.contents

b.value
b[0]
# b[0][0]

b.cont
