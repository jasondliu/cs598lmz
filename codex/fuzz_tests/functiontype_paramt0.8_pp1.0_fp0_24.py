from types import FunctionType
list(FunctionType(g.__code__,globals())(1,2,3))

# %reset

# def f(x,y,z):
#     return [42, None, 'hello']
#
# g = type(f)
# t = g.__new__(g, "<lambda>", f.__code__, f.__globals__, None, None)
# list(t(1,2,3))

class C: pass
obj = C()

def func(): pass

sorted(set(dir(func)) - set(dir(obj)))
# ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__',
# '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']

def clip(text, max_len=80):
    """ Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.
