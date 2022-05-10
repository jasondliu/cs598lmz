fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18493: segfault when calling a builtin function with a bad
# __code__
def segfault():
    class A(object):
        __code__ = None
    A.__call__()

def test_segfault():
    try:
        segfault()
    except TypeError:
        pass
    else:
        raise AssertionError("segfault() should have raised TypeError")

def test_code_attributes():
    def f():
        pass
    co = f.__code__
    assert co.co_filename == __file__
    assert co.co_name == 'f'
    assert co.co_firstlineno == test_code_attributes.__code__.co_firstlineno + 1
    assert co.co_argcount == 0
    assert co.co_flags == 67
    assert co.co_nlocals == 1
    assert co.co_stacksize == 2
    assert co.co_code
    assert co.co_consts
