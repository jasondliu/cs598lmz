fn = lambda: None
# Test fn.__code__
int('1', base=23)
assert (int.__code__.co_varnames[0].startswith('base') == False)
assert (int.__code__.co_freevars == tuple())
assert (int.__code__.co_cellvars == tuple())
# Test fn.__closure__
# Test fn.__globals__
# Test fn.__name__
class B: pass
class C(B):
    def fn(self): pass

assert (C.fn.__name__ == 'fn')
# Test fn.__qualname__
# Test fn.__text_signature__
# Test fn.__module__
# Test fn.__defaults__
# Test fn.__kwdefaults__
# Test fn.__dict__
# Test fn.__doc__
class A:
    def fn(a, b, c=5, *, d, e=7, **kwargs):
        """Docstring"""

def f(): pass
assert (A.fn.__doc__ == "Docstring")
assert (f.__doc
