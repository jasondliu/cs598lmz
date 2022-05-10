gi = (i for i in ())
# Test gi.gi_code.
gi.gi_code
# Test exception propagation.
# NOTE: Test code depends on current implementation details. It is only
#       guaranteed to work with CPython.
# First, with an unpacked generator
def g1(limit):
    for i in range(limit):
        yield i
    yield 0 / 0
def c1(limit):
    print 'started'
    try:
        for i in g1(limit):
            yield i
    except ZeroDivisionError:
        yield 'zero division'
    print 'ending'
for i in c1(3):
    print i

# Second, with a chain of generators.  The chain is
# c1 -> g1 -> g2 -> g3
# where g3 yields an exception. g2 terminates the chain in a 'return'
# in order to force the exception to bubble up to c1.

def g2(it):
    i = 0
    while True:
        try:
            i += 1
            yield it.next()
        except StopIteration:
            return
def g3(limit):
    for
