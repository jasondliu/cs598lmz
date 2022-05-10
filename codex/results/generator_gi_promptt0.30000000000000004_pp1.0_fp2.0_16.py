gi = (i for i in ())
# Test gi.gi_code.co_flags

def f():
    pass

assert f.__code__.co_flags & 0x40 == 0

def f():
    yield

assert f.__code__.co_flags & 0x40

def f():
    yield from (i for i in ())

assert f.__code__.co_flags & 0x40

def f():
    yield from (i for i in ())
    yield

assert f.__code__.co_flags & 0x40

def f():
    yield from (i for i in ())
    yield
    yield from (i for i in ())

assert f.__code__.co_flags & 0x40

def f():
    yield from (i for i in ())
    yield from (i for i in ())

assert f.__code__.co_flags & 0x40

def f():
    yield from (i for i in ())
    yield from (i for i in ())
    yield

assert f.__code__.co_flags & 0x40

def f():
   
