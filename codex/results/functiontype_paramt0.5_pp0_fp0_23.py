from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__).__closure__)

# def f():
#     x = 1
#     def g():
#         print(x)
#     return g
#
# f()()
#
# def f():
#     x = 1
#     def g():
#         print(x)
#     return g
#
# f()()
#
# def f():
#     x = 1
#     def g():
#         print(x)
#     return g
#
# f()()
#
# def f():
#     x = 1
#     def g():
#         print(x)
#     return g
#
# f()()
#
# def f():
#     x = 1
#     def g():
#         print(x)
#     return g
#
# f()()
#
# def f():
#     x = 1
#     def g():
#
