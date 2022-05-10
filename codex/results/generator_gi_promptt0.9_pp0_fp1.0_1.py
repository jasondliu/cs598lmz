gi = (i for i in ())
# Test gi.gi_code is f_getcode

gci = (c for c in ())
# Test gci.gi_code is f_getcode


class C(object):
    def m(self):
        yield 1
        yield 2
        yield 3


gc = C()
mi = gc.m()

# Test methods return gen

# Test that non-local exits call close()
def no_local_return():
    yield 1
    yield 2
    yield 3
    return 5 # should not raise error

def no_local_returnen():
    yield 1
    yield 2
    yield 3
    return None

def no_local_raise():
    try:
        yield 1
        yield 2
        yield 3
    except StopIteration:
        raise

def no_local_generator():
    yield 1
    yield 2
    yield 3

nl1 = [no_local_return(),
       no_local_returnen(),
       no_local_raise(),
       no_local_generator(),]

# Test finally blocks get called by __del__ when an exception
