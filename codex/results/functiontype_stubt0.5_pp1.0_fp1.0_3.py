from types import FunctionType
a = (x for x in [1])
type(a)

isinstance(a, GeneratorType)

def func():
    print('func')

isinstance(func, FunctionType)

isinstance(func, GeneratorType)


def func():
    yield 1
    yield 2
    yield 3

a = func()
isinstance(a, GeneratorType)

next(a)

next(a)

next(a)

next(a)

def func():
    yield 1
    yield 2
    yield 3
    return 10

a = func()

next(a)

next(a)

next(a)

next(a)

def func():
    yield 1
    yield 2
    yield 3
    return 10

a = func()

a.send(None)

a.send(None)

a.send(None)

a.send(None)

a.throw(Exception)

def func():
    try:
        yield 1
        yield 2
        yield 3
    except Exception as e:
        print(e)

