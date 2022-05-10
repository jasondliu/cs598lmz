from types import FunctionType
a = (x for x in [1])
type(a)

b = [lambda : x for x in [1, 2]]
print(b[0]())
print(b[1]())

def test():
    print(1)
    yield 1
    print(2)
    yield 2

t = test()
t.send(None)
t.send(None)

class Test:
    def __init__(self):
        print('test init')

t = Test()

def deco(func):
    def inner():
        print('inner')
    print(func)
    return inner

@deco
def test():
    print('test')

print(type(test))
test()

def deco(func):
    def inner():
        print('inner')
    return inner

@deco
def test():
    print('test')

print(type(test))
test()

class Test:
    def __init__(self):
        print('test init')
    def __call__(self, *args):
        print('call')

t
