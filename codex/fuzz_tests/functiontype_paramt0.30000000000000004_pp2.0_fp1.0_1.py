from types import FunctionType
list(FunctionType(f.__code__, globals(), 'foo'))

# f.__code__.co_freevars
# f.__closure__
# f.__code__.co_cellvars

# def f(x):
#     def g(y):
#         return x + y
#     return g
#
# f(1)(2)
#
# f.__code__.co_freevars
# f.__closure__
# f.__code__.co_cellvars
#
# f.__closure__[0].cell_contents

# def f(x):
#     def g(y):
#         def h(z):
#             return x + y + z
#         return h
#     return g
#
# f(1)(2)(3)
#
# f.__code__.co_freevars
# f.__closure__
# f.__code__.co_cellvars
#
# f.__closure__[0].cell_contents
# f.__closure__[1].cell_cont
