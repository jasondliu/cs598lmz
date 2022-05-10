from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def foo():
    print('in the foo')
    yield 1
    print('in the foo')
    yield 2
    print('in the foo')
    yield 3
    return 'foo'

a = foo()
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def bar():
    print('in the bar')
    return 'bar'

b = bar()
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))

def gen():
    for x in range(10):
        yield x

g = gen()
print(g)
print(isinstance(g, GeneratorType))
print(isinstance(g, FunctionType))

print(g.gi_frame)
print(g.gi_code)
print(g.gi_frame.f_locals)
print(g.gi_frame.f_lasti)
print(g.gi_frame.f_lineno
