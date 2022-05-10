from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(type(a))
print(type(b))
print(dir(a))
print(dir(b))

print(a.gi_frame)
print(b.gi_frame)

print(a.gi_code)
print(b.gi_code)

print(a.gi_running)
print(b.gi_running)


# from types import FunctionType
# from types import GeneratorType
#
# a = (x for x in [1])
# b = (x for x in [2])
#
# print(isinstance(a, FunctionType))
# print(isinstance(b, FunctionType))
#
# print(isinstance(a, GeneratorType))
# print(isinstance(b, GeneratorType))
#
# print(type(a))
# print(type(b))
#
# print(dir(a))
# print(dir(b))
#
# print(a.
