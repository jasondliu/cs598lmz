import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1, 2, 3)

print(fun())
print(type(fun))

@functools.lru_cache(maxsize=None)
def fun(*args, **kwargs):
    return args, kwargs

print(fun(1, 2, 3, x=1, y=2, z=3))
print(fun(1, 2, 3, x=2, y=3, z=4))
print(fun(1, 2, 3, x=1, y=3, z=5))
print(fun.cache_info())
'''

'''
# functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# 将函数包装器的属性更新到被包装的函数上，并且返回被包装的函数。
# 设置了 __wrapped__
