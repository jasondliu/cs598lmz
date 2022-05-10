fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

print(globals() == {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x1095c5898>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': './dummy.py', '__cached__': None, 'fn': <function <lambda> at 0x108ae9ea0>})

print(locals())
fn()
# --------------------------------------------------------------------------------
def f(x):
    y = x + 1
    return y
print(f(10))
# --------------------------------------------------------------------------------
'''
def g(a, b):
    return a + b
g(2, 3)
g('py', 'thon')
'''
# --------------------------------------------------------------------------------
x = 1
print(id(x))
y = 1
print(id(y))
# --------------------------------------------------------------------------------
'''
x = 'something'
y = x
