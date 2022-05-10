import types
# Test types.FunctionType(),types.LambdaType()
print(type(types.FunctionType))  # <class 'type'>
print(type(lambda x:x))          # <class 'function'>

# What is FunctionType()
# It is a function.
# FunctionType() will create a function.

def func1(n):
    n += 1
    return n

func2 = types.FunctionType(func1.__code__,
                           func1.__globals__,
                           func1.__name__,
                           func1.__defaults__,
                           func1.__closure__)

print(func1(1))     # 2
print(func2(2))     # 3

# To understand what I mean,
# Let us see the magic of FunctionType()
# print(func1.__code__)
# <code object func1 at 0x040C8990, file "D:/Type.py", line 10>
# print(func1.__globals__)
# {'__loader__': <_frozen_importlib_external.
