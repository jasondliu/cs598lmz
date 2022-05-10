from types import FunctionType
a = (x for x in [1])
print(a.__next__())

print((lambda x: x > 2)(3))


def test(x):
    return x+1


tf = FunctionType(test.__code__, test.__globals__, "newname")
print(tf(3))


def aa():
    print(1)
    yield
    print(2)


for x in aa():
    pass

a = (x for x in [1])
print(a.__next__())

print((lambda x: x > 2)(3))


def test(x):
    return x+1


tf = FunctionType(test.__code__, test.__globals__, "newname")
print(tf(3))


def aa():
    print(1)
    yield
    print(2)


for x in aa():
    pass

test = {}
test.setdefault("key0", []).append(1)
test.setdefault("key0", []).append(2)
test.setdefault("key1", []
