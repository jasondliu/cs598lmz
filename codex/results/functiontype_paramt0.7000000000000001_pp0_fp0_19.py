from types import FunctionType
list(FunctionType())

a = 1
def test():
    a = 2
    print(a)
print(a)
test()
print(a)

def test():
    global a
    a = 2
    print(a)
print(a)
test()
print(a)

a = 1
def test():
    a = 2
    print(a)
    return a
print(a)
a = test()
print(a)

def test():
    print(1)
    return 1
    print(2)
    return 2
print(test())

def test():
    return 1, 2
a, b = test()
print(a)
print(b)

def test():
    return (1, 2)
a, b = test()
print(a)
print(b)

def test():
    return [1, 2]
a, b = test()
print(a)
print(b)

def test():
    return [1, 2, 3]
a, b = test()
print(a)
print(b)
