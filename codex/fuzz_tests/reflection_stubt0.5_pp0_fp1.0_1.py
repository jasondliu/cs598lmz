fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "fn"
fn.__dict__ = {}

# Test the C API

def test_PyEval_EvalCode():
    d = {}
    g = {}
    l = {}
    c = compile("1 + 1", "<string>", "eval")
    assert eval(c, g, l) == 2
    assert eval(c, d) == 2
    assert eval(c) == 2
    raises(TypeError, eval, 42, 42, 42)
    raises(TypeError, eval, 42, 42)
    raises(TypeError, eval, 42)
    c = compile("1 + 1", "<string>", "exec")
    raises(TypeError, eval, c)
    exec(c, g, l)
    exec(c, d)
    exec(c)
    raises(TypeError, exec, c, g, l, 42)
    raises(TypeError, exec, c, d, 42)
    raises(TypeError, exec, c, 42)
    raises(TypeError, exec, 42
