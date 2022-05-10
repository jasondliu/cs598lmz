fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class InheritanceWithCode(object):
    def __init__(self, *args, **kw):
        pass


def create_local_inheritance_with_code():
    class MyClass(InheritanceWithCode):
        pass

    m = MyClass()


def mk_generator():
    def gen():
        yield 1

    return gen(), gen


def iter_exception_no_stopiteration_inherited(stop):
    try:
        iter(stop)
    except Exception:
        pass


class A(object):
    pass


class StopIterationWithNewStyleException(StopIteration, A):
    pass


def iter_exception_new_style_exception_inherited_from(stop):
    try:
        iter(stop)
    except Exception:
        pass
