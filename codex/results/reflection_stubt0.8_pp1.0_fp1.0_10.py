fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi

class C:
    def __init__(self):
        pass

c = C()
c.__reduce__ = fn
del fn
c.__reduce__()
