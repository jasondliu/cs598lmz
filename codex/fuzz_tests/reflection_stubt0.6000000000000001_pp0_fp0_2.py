fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# issue #7
def test_function_repr():
    def f(): pass
    assert repr(f) == "<function f at 0x%x>" % id(f)

def test_function_repr_module_name():
    import sys
    m = sys.modules['__main__']
    def f(): pass
    m.f = f
    assert repr(f).startswith("<function f at 0x%x>" % id(f))
    assert repr(f).endswith(">")

def test_function_dir():
    def f(): pass
    names = dir(f)
    assert '__name__' in names
    assert '__module__' in names
    assert '__code__' in names
    assert '__defaults__' in names
    assert '__dict__' in names
    assert '__doc__' in names
    assert '__globals__' in names

def test_function_code():
    def f(): pass
    assert type(f.__code__)
