from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code objects
def f(x):
    return x

list(f.__code__)

# method objects
class C:
    def m(self, x):
        return x

list(C.m)

# module objects
import sys
list(sys)

# generator objects
def g():
    yield 1
    yield 2

list(g())

# coroutine objects
async def c():
    await 1
    await 2

list(c())

# async generator objects
async def ag():
    yield 1
    yield 2

list(ag())

# traceback objects
try:
    1/0
except Exception as e:
    tb = e.__traceback__

list(tb)

# frame objects
def f():
    1/0

try:
    f()
except Exception as e:
    tb = e.__traceback__
    f = tb.tb_frame

list(f)

# dict proxy objects
