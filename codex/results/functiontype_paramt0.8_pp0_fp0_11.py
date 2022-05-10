from types import FunctionType
list(FunctionType(
    f.__code__, globals(), f.__name__, f.__defaults__, 
    f.__closure__).__closure__)

# (<cell at 0x7f46e03c66b8: int object at 0x7f46e02344c0>,)
# return [c.cell_contents for c in f.__closure__]

def b(x):
    return a(x)

b.__closure__

# (<cell at 0x7f46e03c66b8: int object at 0x7f46e02344c0>,)
# return [c.cell_contents for c in f.__closure__]
a.__dict__['y']
# <function __main__.a.<locals>.x>
a.__dir__()
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__
