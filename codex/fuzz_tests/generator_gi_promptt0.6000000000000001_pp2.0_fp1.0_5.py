gi = (i for i in ())
# Test gi.gi_code

def f1():
    yield 1
    yield 2

def f2():
    yield 1
    return
    yield 2

def f3():
    yield 1
    raise StopIteration
    yield 2

def f4():
    yield 1
    raise RuntimeError
    yield 2

def f5():
    yield 1
    1/0
    yield 2

def test_gi_code():
    assert f1().gi_code == f1.__code__
    assert f2().gi_code == f2.__code__
    assert f3().gi_code == f3.__code__
    assert f4().gi_code == f4.__code__
    assert f5().gi_code == f5.__code__

# Test gi_frame

def f1():
    a = 1
    yield 1
    yield 2

def f2():
    a = 1
    yield 1
    return
    yield 2

def f3():
    a = 1
    yield 1
    raise StopIteration
    yield 2

def
