from types import FunctionType
a = (x for x in [1])
b = a.__iter__
c = b.__func__
assert c == iter
assert isinstance(c, FunctionType)
assert not isinstance(c, type)
assert isinstance(iter, type)
assert isinstance(iter, FunctionType)
assert not hasattr(c, '__call__')

# Issue #28422: __copy__() and __deepcopy__() methods of methods obtained
# from __func__ and im_func should return None.
class C:
    def f(self):
        pass

def test():
    m = C.f
    for i in m, type(C).f.__func__:
        assert i.__copy__() is None
        assert i.__deepcopy__(None) is None

test()
