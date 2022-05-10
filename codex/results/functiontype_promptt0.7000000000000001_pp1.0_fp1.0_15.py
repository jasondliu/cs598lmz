import types
# Test types.FunctionType, types.LambdaType, etc.
# Many of these tests require that the function is executed in its own
# environment.

def gen_empty():
    pass

def gen_single_yield():
    yield 1

def gen_multi_yield():
    yield 1
    yield 2

def gen_return():
    return 1

def gen_raise():
    raise StopIteration

def gen_yield_return():
    yield 1
    return 1

def gen_yield_raise():
    yield 1
    raise StopIteration

def gen_yield_from():
    yield from [1, 2, 3]

def gen_yield_from_return():
    yield from [1, 2, 3]
    return

def gen_yield_from_multi_yield():
    yield from [1, 2, 3]
    for i in range(4, 7):
        yield i

def gen_yield_from_multi_yield_return():
    yield from [1, 2, 3]
    for i in range
