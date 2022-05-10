import weakref
# Test weakref.ref() and weakref.proxy() with callable objects

class FooCallable(object):
    def __call__(self):
        return '__call__'
    def __str__(self):
        return '__str__'
    def __repr__(self):
        return '__repr__'

class BarCallable(object):
    def __call__(self):
        raise RuntimeError('dummy')
    def __str__(self):
        return '__str__'
    def __repr__(self):
        return '__repr__'

def Check(x):
    #print(repr(x), end='')
    try:
        print(x())
    except Exception as msg:
        print(msg)


for obj in [
        FooCallable(),
        BarCallable()
        ]:
    print(repr(obj), end=' ')
    Check(obj)
    print(str(obj), end=' ')
    Check(str)
    print(repr(obj), end=' ')
    Check
