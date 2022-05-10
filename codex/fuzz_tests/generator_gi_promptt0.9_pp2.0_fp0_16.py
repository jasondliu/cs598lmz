gi = (i for i in ())
# Test gi.gi_code
setattr(gi, 'gi_code', None)


# Test weakref on iterators.
# See http://bugs.python.org/issue11739 for iterators -- still true for 3.2.2
# See http://bugs.python.org/issue11786 for generators
# Only this weakref-related regrtest fails can flag a problem with these tests
def gen(x):
    i = 0
    while 1:
        yield i


it = gen(1)
wr = weakref.ref(it)
if wr() is not it:
    raise RuntimeError("weakref test 1: %r" % (wr(),))
next(it)
if wr() is not it:
    raise RuntimeError("weakref test 2: %r" % (wr(),))
del it
if wr() is not None:
    raise RuntimeError("weakref test 3: %r" % (wr(),))

# Callable generator
def foo():
    n = 0
    while True:
        n += 1
        yield n

def bar():
    n = 5
    y = foo
