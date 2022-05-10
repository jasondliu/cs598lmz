gi = (i for i in ())
# Test gi.gi_code

def f():
    yield 1
    yield 2

gi = f()
assert gi.gi_code is f.__code__

def f():
    yield 1
    yield 2
    return

gi = f()
assert gi.gi_code is f.__code__

def f():
    pass

gi = f()
assert gi.gi_code is f.__code__

def f():
    try:
        yield 1
    except:
        yield 2
    else:
        yield 3
    finally:
        yield 4

gi = f()
assert gi.gi_code is f.__code__

def f():
    try:
        yield 1
    except:
        yield 2
    else:
        yield 3
    finally:
        yield 4
    return

gi = f()
assert gi.gi_code is f.__code__

def f():
    try:
        pass
    except:
        yield 2
    else:
        yield 3
    finally:
        yield 4

gi = f
