fn = lambda: None
# Test fn.__code__ and extensions to __code__
setattr(fn, '__code__', 42); raises(TypeError, fn.__code__.co_kwonlyargcount)
setattr(fn, '__code__', b'abc'); raises(TypeError, fn.__code__.co_kwonlyargcount)
class A:
    pass
setattr(fn, '__code__', A()); raises(TypeError, fn.__code__.co_kwonlyargcount)

def unbound_method_is_not_a_function():
    class A:
        def f(self):
            pass
    A.f()
raises(TypeError, unbound_method_is_not_a_function)

class B:
    def __eq__(self, other):
        raise NotImplementedError

def check_cmp(type_):
    fn = type_()
    raises(TypeError, cmp, fn, 1)
    raises(TypeError, cmp, 1, fn)
    raises(TypeError, cmp, fn, B())
    raises(TypeError,
