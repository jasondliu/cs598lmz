import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def f(x, y):
    return (x+1.)*(y+1.)

c_f = FUNTYPE(f)
func = C.Function()
func.set_function(c_f)

a = func.call(C.double(-1.), C.double(-2.))
print(a)

# %%
# The C++ function is compiled on the fly.
#
# The function is compiled on the fly from the C++ string.

func = C.Function()
func.set_function('''
    return (x+1.)*(y+1.);
''')

a = func.call(C.double(-1.), C.double(-2.))
print(a)

# %%
# The C++ function is compiled on the fly.
#
# The function is compiled on the fly from the C++ string.

func = C.Function()
func.set_function('''
    return (x+1.)*(y+
