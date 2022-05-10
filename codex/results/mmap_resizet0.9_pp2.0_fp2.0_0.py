import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

class A1(A2):
    def __new__(cls):
        self = A2.__new__(A1)
        return self

def check_args(args, kwargs):
    return args, kwargs

def test_args(*args, **kwargs):
    return check_args(args, kwargs)

def test_kwargs(x='x', y='y'):
    return check_args([], locals())

def test_xx(x, *args):
    return check_args(args, {})

def test_yy(*args):
    return check_args(args, {})

def test_xyx(x, *args, y=10):
    return check_args(args, locals())

def test_xxy(x, *args, y=10):
    return check_args(args, locals())

def test_xyxx(x, *args, y=10, **kwargs):
    return check_args(args, kwargs)

kwargs = dict
