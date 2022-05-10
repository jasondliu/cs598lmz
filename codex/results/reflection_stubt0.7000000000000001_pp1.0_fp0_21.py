fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__globals__ = fn.__dict__ = {'__builtins__': {}}

with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    fn()
    assert len(w) == 1
    assert issubclass(w[0].category, RuntimeWarning)
    assert "__code__" in str(w[0].message)
    assert "__builtins__" in str(w[0].message)

# Issue #16132: If the closure is missing, a TypeError should be raised
# instead of a RuntimeWarning.
def f():
    x = 1
    def g():
        print(x)
        return 1

    return g

g = f()
g.__code__ = (i for i in ()).gi_code

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    with pytest.raises(TypeError):
        g()

def f():
    x = 1
    def g():
       
