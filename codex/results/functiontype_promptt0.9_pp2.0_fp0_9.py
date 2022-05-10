import types
# Test types.FunctionType type
def f_f_get(obj, objtype=None):
    if objtype is None:
        objtype = type(obj)
    if objtype == types.FunctionType:
        return obj.__code__
    return None


def f_f_init(obj, src):
    obj.__code__ = src
    return


def f_f_copy(obj):
    return types.FunctionType(obj.__code__, obj.__globals__, obj.__name__,
        obj.__defaults__, obj.__closure__)


f_f_get.names = [' FunctionType', 'get']
f_f_init.names = [' FunctionType', 'init']
f_f_copy.names = [' FunctionType', 'copy']
dict_setitem(' FunctionType', 'get', f_f_get)
dict_setitem(' FunctionType', 'init', f_f_init)
dict_setitem(' FunctionType', 'copy', f_f_copy)
# Test types.ClassType type
def f_c_get(obj
