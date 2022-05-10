import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callfn(x, y):
    return x + 2 * y

fn = FUNTYPE(callfn)
print(fn(1, 2))

# Calling Python callables
print("-" * 78)

class Foo:
    def __init__(self):
        self.counter = 0

    def __call__(self, x, y):
        self.counter += 1
        return x + 2 * y

foo = Foo()
fn = FUNTYPE(foo)
print(fn(1, 2))
print(fn(2, 3))
print(foo.counter)
