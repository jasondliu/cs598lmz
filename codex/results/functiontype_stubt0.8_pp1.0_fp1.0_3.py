from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(iter(b)))
print(type(iter(a)))
print(type(a))
print(type(b))
print(type(map))
print(type(FunctionType))

print(dir(map))

print(dir(FunctionType))


# try:
#     raise NameError('HiThere')
# except NameError as e:
#     print("An exception flew by!")
#     raise
