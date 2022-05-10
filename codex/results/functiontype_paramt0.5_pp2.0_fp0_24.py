from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__).__code__.co_freevars)

# The following code is equivalent to:
#     def f(x):
#         def g(y):
#             return x + y
#         return g
#
#     import dis
#     dis.dis(f)
#
# It produces the following output:
#     2           0 LOAD_CONST               1 (<code object g at 0x10e0a5c70, file "<dis>", line 2>)
#                 3 MAKE_FUNCTION            0
#                 6 STORE_FAST               1 (g)
#
#     3           9 LOAD_FAST                1 (g)
#                12 RETURN_VALUE
#
#     4     >>   13 LOAD_CLOSURE             0 (x)
#                16 LOAD_DEREF               0 (x)
#                19 LOAD_FAST                0 (y)
#                22 BINARY_ADD
#
