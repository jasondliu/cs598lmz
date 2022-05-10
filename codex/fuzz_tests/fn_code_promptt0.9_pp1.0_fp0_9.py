fn = lambda: None
# Test fn.__code__.co_varnames to ensure it's not a function (compare to bool)
setattr(bool, '__code__', bool.__code__)
setattr(fn, '__code__', bool.__code__)
print(repr(dir(fn)))
print(dir(fn.__code__))
print('co_varnames' in dir(fn.__code__))
print('co_varnames' in dir(bool.__code__))
print(fn.__code__.co_varnames)
print('co_varnames' in dir(fn.__code__))


class A(object):
    def __gt__(self, other):
        raise NotImplementedError


print(A() > 5)


class B(object):
    def __gt__(self, other):
        raise NotImplementedError()


print(isinstance(NotImplementedError, type))
print(isinstance(A(), object))
print(issubclass(A, object))
print(issubclass(NotImplementedError, Base
