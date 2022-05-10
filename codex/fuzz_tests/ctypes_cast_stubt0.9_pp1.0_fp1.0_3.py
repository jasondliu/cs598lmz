import ctypes
ctypes.cast(g, ctypes.POINTER(foo)).contents

# this is safer
# but you then don't have to worry about trying to cast them in C
f = foo.foo()
g = foo.dyn()
g.contents = f
g.contents

# and you can iterate over it
for x in g:
    print x
