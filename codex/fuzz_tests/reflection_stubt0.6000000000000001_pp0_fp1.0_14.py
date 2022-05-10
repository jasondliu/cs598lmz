fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(
    0, 0, 0, 0, b"", b"", (), (), (), "", b"", 0, b"")
fn.__code__.co_varnames = gi.gi_code.co_varnames = ()
fn.__code__.co_argcount = gi.gi_code.co_argcount = 0

def test_gen_send():
    def gen():
        yield 1
        yield 2
    g = gen()
    g.send(None)
    raises(TypeError, g.send, None)

def test_gen_iter_send():
    def gen():
        yield 1
        yield 2
    g = gen()
    raises(TypeError, iter, g)
    g.send(None)
    raises(TypeError, next, g)
    raises(TypeError, g.send, None)

def test_gen_throw():
    def gen():
        yield 1
        yield 2
        yield 3
    g = gen()
    g.send(None)
