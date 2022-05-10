import ctypes
ctypes.cast(id(id(42)), ctypes.py_object)

# first(42)

# print(id(id), id(first), id(first(42)), id(second(42)), id(id(42)))

# print(first is id)
# print(first(42) is id(42))
# print(first(42) is second(42))
# print(second is id)
# print(second(42) is id(42))

# print(first(42) is id(id(42)))

# print(first(42) == second(42))
# print(first(42) == id(42))
# print(first(42) == id(id(42)))

# print(first(42))
# print(id(42))
# print(id(id(42)) is id(id(42)))

# print(id(id(42)))

# id = first
# print(id(42) is id(42))
# print(id(42) is first(42))

# def func():
#   return 42
#
