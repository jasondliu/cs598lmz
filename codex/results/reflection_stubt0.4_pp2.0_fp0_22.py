fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the interpreter doesn't crash when an exception is raised
# from a generator's iterator.next() method.
def gen_iter():
    yield 1
    yield 2
    raise StopIteration

def gen():
    yield 1
    yield 2
    raise StopIteration

def gen_exc():
    yield 1
    yield 2
    raise RuntimeError

def gen_finally():
    try:
        yield 1
    except:
        pass
    else:
        yield 2
    finally:
        yield 3
    yield 4

class StopIter(Exception):
    pass

def gen_stopiter():
    yield 1
    yield 2
    raise StopIter

def gen_yield_stopiter():
    yield 1
    yield 2
    yield StopIter

def gen_return():
    yield 1
    yield 2
    return

def gen_yield_return():
    yield 1
    yield 2
    yield None

class Stop(Exception):
    pass

def gen_stop():
    yield 1
    yield 2
