gi = (i for i in ())
# Test gi.gi_code is nullptr
gi
# Test gi.gi_frame is nullptr
gi.gi_frame

def g():
    yield 1
    yield 2

g.gi_code is g.__code__
g.gi_frame is g.__globals__

# Test compiling a generator with a yield with a non-trivial __del__

import types

def g():
    def f():
        yield 1
    return f

g().gi_code.co_flags & types.CO_GENERATOR

class A:
    def __del__(self):
        pass

def g():
    yield A()

g().gi_code.co_flags & types.CO_GENERATOR

# Test generator throws IndexError on empty generator

def g():
    yield

try:
    next(g())
    raise Exception("no error")
except StopIteration as e:
    pass

try:
    next(g())
    raise Exception("no error")
except StopIteration as e:
    pass

# Test generator throws IndexError
