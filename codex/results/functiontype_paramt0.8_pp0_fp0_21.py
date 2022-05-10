from types import FunctionType
list(FunctionType(function).__globals__.keys())

# [i for i in dir(function) if not i.startswith('_')]

# def getnames(func):
#     k = list(FunctionType(function).__globals__.keys())
#     a = [i for i in dir(function)]
#     print(k, a)
#
# getnames(function)
#
# print(function.__code__.co_names)
# print(function.__code__.co_varnames)
# print(function.__code__.co_argcount)

# x = [1, 2, 3]
# y = "abc"
# z = [0]
# z.append(x)
# z.append(y)
# print(z)
# print(z.index(x))
# print(z.index(y))
