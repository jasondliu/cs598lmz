from types import FunctionType
list(FunctionType(lambda: 1, {}).__closure__)  # [1]
list(FunctionType(lambda: 1, {}, {}).__closure__)
list(FunctionType(lambda: 1, {}, {}, None).__closure__)
list(FunctionType(lambda: 1, {}, {}, {}).__closure__)
list(FunctionType(lambda: 1, {}, {}, {}, "annotations").__closure__)

# The following is equivalent to:
# def f():
#     return 1
# f.__closure__ = (1,)
FunctionType(lambda: 1, {}, {}, {}, "annotations", "kwdefaults")

# Should be able to create a function from a code object
def f():
    pass
f2 = FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)
f2()  # should not raise an exception

def f():
    pass
c = f.__code__
g = FunctionType(c, {}, "test", (), None)

