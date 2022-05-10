import weakref
# Test weakref.ref() on an exception object.
class BaseError(Exception):
    pass

class DerivedError(BaseError):
    pass

def raiseBaseError():
    raise BaseError

def raiseDerivedError():
    raise DerivedError


for factory in [BaseError, DerivedError]:
    wr = weakref.ref(factory())
    assert wr() is None, wr
    assert wr() is None, wr
    assert wr() is None, wr
    assert wr() is None, wr
    assert wr() is None, wr
    assert wr() is None, wr
    assert wr() is None, wr
    assert wr() is None, wr
    assert wr() is None, wr
    assert wr() is None, wr
    assert wr() is None, wr
    assert wr() is None, wr
    assert wr() is None, wr


for constructor in [BaseError, DerivedError]:
    try:
        raise constructor
    except Exception as exc:
        wr = weakref.ref(exc)
        assert wr() is exc, wr
        assert wr() is exc, wr

