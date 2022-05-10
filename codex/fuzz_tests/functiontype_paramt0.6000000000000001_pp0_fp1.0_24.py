from types import FunctionType
list(FunctionType(f.__code__, globals(), "some_name"))

# @typechecked
# def f(x: str) -> int:
#     return 4
#
#
# print(f("3"))
# print(f(3))
