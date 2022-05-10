import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('here')
    return None

print(fun())

@functools.singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)

#@fun.register(list)
#def _(arg, verbose=False):
#    if verbose:
#        print("Enumerate this:")
#    for i, elem in enumerate(arg):
#        print(i, elem)

fun([1,2,3])
fun(np.array([1,2,3]), verbose=True)


@fun.register(pd.DataFrame)
def _(arg, verbose=False):
    if verbose:
        print("Enumerate this:")
    return arg.to_string()

fun(pd.
