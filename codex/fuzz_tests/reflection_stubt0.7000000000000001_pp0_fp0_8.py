fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

class C(metaclass=type):
    def __init__(cls, *args, **kwargs):
        super().__init__()
        raise Exception

c = C()

class D(metaclass=C):
    pass

try:
    d = D()
except Exception:
    pass

print(d)
