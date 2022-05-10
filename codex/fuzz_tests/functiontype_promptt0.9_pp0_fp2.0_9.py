import types
# Test types.FunctionType in Python 3.4.4

class Foo(object):
    def __init__(self, f):
        assert type(f) is types.FunctionType
        assert f.__name__ == "f"
        assert f.__doc__ == "fdoc"
        assert type(f.__code__) is types.CodeType
        assert f.__code__.co_argcount == 2
        assert f.__code__.co_nlocals == 2
        assert f.__code__.co_code == b'd\x01}\x01s\x02\x00\x83\x01\x01s\x01\x00'
        assert f.__code__.co_cellvars == ('x',)
        assert f.__code__.co_freevars == ('y',)
        assert f.__self__ is None
        assert f.__dict__ == {}

def f(x):
    global y
    return x + y
f.__code__ = types.CodeType(2, 2, 0, 1, b'd\x01}\
