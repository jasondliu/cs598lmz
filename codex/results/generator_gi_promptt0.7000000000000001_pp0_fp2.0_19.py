gi = (i for i in ())
# Test gi.gi_code is None
def f():
    yield
f.func_closure = (gi,)
def f():
    yield 1
f.func_closure = (gi,)
def f():
    yield 1,2,3
f.func_closure = (gi,)
def f():
    yield 1,2,3
    return 4
f.func_closure = (gi,)
def f():
    yield 1,2,3
    raise StopIteration
f.func_closure = (gi,)
def f():
    raise StopIteration
f.func_closure = (gi,)
def f():
    return
f.func_closure = (gi,)
def f():
    return 1
f.func_closure = (gi,)
def f():
    return 1,2,3
f.func_closure = (gi,)
def f():
    return 1,2,3
    raise StopIteration
f.func_closure = (gi,)
def f():
    return 1,2,3
    raise RuntimeError
f.func_closure = (gi,)
def f():
    raise StopIteration
