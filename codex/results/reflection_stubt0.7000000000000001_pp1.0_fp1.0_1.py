fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

print(fn())

# 2.
class MyDict(dict):
    def __missing__(self, key):
        print(self, key)
        return 1

d = MyDict()

print(d.get('a'))
print(d.get('b'))
print(d)

# 3.

print('\n------')

def fn(arg1, arg2, *argv, kwarg1, kwarg2=None, **kwargv):
    print(arg1, arg2, argv, kwarg1, kwarg2, kwargv)

fn(1, 2, 3, kwarg1=4, kwarg2=5)

print('\n------')

# 4.
# Нет примера

# 5.
print('\n------')

def fn(f):
    print(f)

fn(fn)

print('\n------')

# 6.
print('\n------')


