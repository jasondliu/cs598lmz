import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

def f():
    return view[0]

def g(x):
    view[0] = x

def h():
    view[0] = 0

def run_iter(it):
    try:
        while True:
            next(it)
    except StopIteration:
        pass

def test_read_and_write():
    assert f() == 0
    g(1)
    assert f() == 1
    g(2)
    assert f() == 2
    h()
    assert f() == 0

def test_read_and_write_in_generator():
    def gen():
        yield f()
        g(1)
        yield f()
        g(2)
        yield f()
        h()
        yield f()
    run_iter(gen())

def test_read_and_write_in_generator_with_stopiteration():
    def gen():
        yield f()
        g(1)
        yield f()
        g(2)
        yield f()
        h()
        yield
