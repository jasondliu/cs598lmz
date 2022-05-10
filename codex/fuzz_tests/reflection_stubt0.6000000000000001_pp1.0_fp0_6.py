fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
fn.__code__ = None
fn()

# This test is not relevant for PyPy
if not is_pypy:
    # Test code.__code__
    def f():
        pass
    def g():
        return f.__code__
    x = g()
    print(type(x), x.co_name, x.co_filename)
    if f.__code__ is not g.__code__:
        print('bug in Python implementation')
    # Test code.__dict__
    def h():
        pass
    try:
        h.__code__.__dict__
    except AttributeError:
        print('no __dict__')
    else:
        print('has __dict__')
    try:
        h.__code__.__dict__ = {}
    except TypeError:
        print('__dict__ is read-only')
    else:
        print('__dict__ is writeable')
    # Test code.__reduce__
    def i():
        pass
    r = i.__code__
