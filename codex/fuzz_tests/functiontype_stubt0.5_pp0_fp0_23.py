from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(dir(a))
print(a.gi_code)
print(a.gi_frame)
print(a.gi_running)

print(a.__next__())
print(a.__next__())

# print(next(a))
# print(next(a))

# print(a.send(None))
# print(a.send(None))

# print(a.__next__())
# print(a.__next__())

print(a.gi_frame)
print(a.gi_running)
