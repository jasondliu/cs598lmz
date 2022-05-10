import types
# Test types.FunctionType
def f(x):
    return x + 2

assert type(f) == types.FunctionType
# Test types.LambdaType
f = lambda x: x + 2

assert type(f) == types.LambdaType
# Test types.GeneratorType
def f(x):
    yield x + 2

assert type(f(2)) == types.GeneratorType
# Test types.GeneratorType
def f(x):
    yield from x

assert type(f(range(10))) == types.GeneratorType
# Test types.GeneratorType
def f(x):
    for i in x:
        yield i

assert type(f(range(10))) == types.GeneratorType
# Test types.GeneratorType
def f(x):
    try:
        yield x
    except:
        yield x

assert type(f(2)) == types.GeneratorType
# Test types.GeneratorType
def f(x):
    try:
        yield x
    finally:
        yield x

assert type(f(2)) == types
