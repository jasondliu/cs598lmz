from types import FunctionType
a = (x for x in [1])
print(type(a))
b = [1]
print(type(b))
c = {}
print(type(c))
d = FunctionType
print(type(d))
print("--------------------------------")
try:
    print("test1")
    # raise NameError("test2")
except NameError as e:
    print("test3", e)
else:
    print("test4")
finally:
    print("test5")
