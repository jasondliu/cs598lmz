import io
# Test io.RawIOBase
x = io.RawIOBase()

# Test exceptions
class Error(Exception):
    pass

class MyException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class Raiser:
    def __init__(self, x):
        self._x = x

    def __getattr__(self, name):
        if name == 'x':
            return self._x
        raise AttributeError(name)

    def __repr__(self):
        return "<Raiser %d>" % self._x

class Uninferrable:
    def __str__(self):
        return 'Uninferrable'

def foo():
    raise Error

# Test typing.Union



class A:
    pass

class B(A):
    pass

class C(B):
    pass

