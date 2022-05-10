fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = ''

def f(*args):
    pass


class F():

    def fn(*args):
        pass
