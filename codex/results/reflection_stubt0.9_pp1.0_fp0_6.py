fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def x():
    def bar():
        pass


def x():
    def bar():
        pass
    yield bar
fn = x()
fn.gi_frame.f_code = lambda: None


def x():
    def bar():
        pass
    return bar
fn = x()
fn.__code__ = W_Graph(fn).as_code()
