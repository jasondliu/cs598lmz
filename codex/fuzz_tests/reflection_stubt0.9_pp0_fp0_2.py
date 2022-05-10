fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi  # shouldn't raise but shouldn't succeed


del fn
del gi

# Test names
def f():
    locals()['f'] = 1
    globals()['f'] = 2
    f                   # this should access the local
print(f())
del f

print(locals()['__builtins__'])
print(globals()['__builtins__'])
print(locals()['__builtins__'] is globals()['__builtins__'])

print(locals())
print(globals())
print(locals() is globals())
l = locals()
globals()['__bau'] = 3
print('__bau' in l)

# Test mixed locals and globals
def f(x):
    x = 2
    y = x
    print(locals() is not globals())
    print(locals())
    print(globals())

f(1)
del f

class X:
    def f(self):
        print(self is locals()['self'])

x
