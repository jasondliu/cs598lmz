import ctypes
# Test ctypes.CFUNCTYPE debugging hooks
if ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 42)() != 42:
    raise Exception("ctypes.CFUNCTYPE failed")
if ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 2)(40) != 42:
    raise Exception("ctypes.CFUNCTYPE failed")
# Test calling a module's builtin function from another module
class UserClass:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return (isinstance(other, UserClass)
                and (self.value == other.value))


from test.support import import_fresh_module
with import_fresh_module('marshal', fresh=[__name__]):
    from marshal import dumps, loads

    print('ctypes test 1')
    uc = UserClass(42)
    ud = loads(dumps(uc))
    if uc != ud:
        raise Exception("marshalling User
