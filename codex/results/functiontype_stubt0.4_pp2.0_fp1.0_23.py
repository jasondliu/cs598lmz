from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(FunctionType))

def test():
    print("test")

print(type(test))
print(type(test()) == None)

def test1():
    print("test")
    return 1

print(type(test1()))

def test2(x):
    print("test")
    return x

print(type(test2(1)))

def test3(x):
    print("test")
    return x, 1

print(type(test3(1)))

def test4(x):
    print("test")
    return [x, 1]

print(type(test4(1)))

def test5(x):
    print("test")
    return (x, 1)

print(type(test5(1)))

def test6(x):
    print("test")
    return {x, 1}

print(type(test6(1)))

def test7(x):
    print("test")
    return {x: 1}

print(
