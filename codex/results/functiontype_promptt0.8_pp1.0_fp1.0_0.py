import types
# Test types.FunctionType
def foo():
    a = 1
    b = 2
    return True

t = foo

print type(t)
print type(foo)

print t()

# Test types.LambdaType
t = lambda x: x * 2

print t(5)

# Test types.GeneratorType
def gen():
    for i in range(10):
        yield i * 2

t = gen

print type(t)
print type(gen)
for i in t():
    print i,
print

def double_range(start, stop, step=1):
    x = start
    while x < stop:
        yield x
        x += step
        yield x
        x += step

t = double_range(1, 11, 3)

for i in t:
    print i,
print

# Test types.ModuleType
import string

t = string

print type(t)
print type(string)
print string

# Test types.ClassType
def func():
    pass

class Klass:
    def
