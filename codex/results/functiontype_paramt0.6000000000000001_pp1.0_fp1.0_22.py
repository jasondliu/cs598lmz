from types import FunctionType
list(FunctionType(f.func_code, f.func_globals).func_closure)

# x = 10
#
# def foo():
#     # x = 5
#     y = 2
#     def bar():
#         # x = 1
#         def baz():
#             print x
#
#         baz()
#     bar()
#
# foo()
#
# def foo():
#     def bar():
#         def baz():
#             print x
#         baz()
#     x = 5
#     bar()
#
# foo()


# def foo():
#     x = 5
#     def bar():
#         x = 1
#         def baz():
#             print x
#         baz()
#     bar()
#
# foo()
#
# def foo():
#     def bar():
#         def baz():
#             print x
#         x = 1
#         baz()
#     x = 5
#     bar()
#
# foo()
#
# def foo():
#     def bar
