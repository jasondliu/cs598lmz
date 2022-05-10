import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

f1 = fun()
f2 = fun()
assert f1 is f2

# this is a bug in ctypes and will be fixed in 3.2
# https://sourceforge.net/p/ctypes/bugs/280/
#assert f1 == f2

# we can use globals() to get only the globals in the current module
# by setting the module name here, we can use this function in other modules
# without having to import the module name

def get_globals(module=None):
    if module is None:
        module = __name__
    def get_globals_closure():
        return globals().copy()
    return get_globals_closure

# now we can use get_globals in another module
# to get the globals in that module

# the function can be used in a module like this

# import functools
# import some_other_module
# globals = functools.partial(some_other_module.get_globals, __name__)()

# print
