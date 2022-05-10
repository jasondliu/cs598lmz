fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class T:
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def __lt__(self, other):
        return NotImplemented


class SubT(T):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        pass

    def __lt__(self, other):
        return NotImplemented


class A(T):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        pass

    def __lt__(self, other):
       
