from types import FunctionType
a = (x for x in [1])
next(a)

b = iter([1])
next(b)

def work1(iter):
    print(next(iter))

work1(b)

def work2(iter):
    while True:
        try:
            print(next(iter))
        except StopIteration as e:
            break


work2(b)

work2(a)

def func():
    yield 1
    yield 2
    yield 3


f = func()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# next(f)


def func1(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(func(*args, **kwargs))

    return wrapper

@func1
def demo():
    return 'demo'

# demo = func1(demo)
# demo()


def func2(func):
    def wrapper(*args, **kwargs):
        print(func.__
