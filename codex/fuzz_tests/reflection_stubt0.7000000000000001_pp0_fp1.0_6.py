fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
getattr(fn, '__code__')()
"""
    assert optimizer.count_ops(src) == 1
    assert optimizer.remove_ext_attributes(src) == src


def test_builtin_simple_inplace_attribute(space):
    src = """
def fn():
    x = abc.__dict__
    x['a'] = 1
    del x['b']
abc.__dict__ = x
abc.__dict__[0] = 1
abc.__dict__[1] = 2
abc.__dict__[2] = 3
"""
    assert optimizer.count_ops(src) == 16
    assert optimizer.remove_builtin_simple_inplace_attribute(src) == """
def fn():
    x = abc.__dict__
    x['a'] = 1
    del x['b']
abc.__dict__ = x
abc.__dict__[0] = 1
abc.__dict__[1] = 2
abc.__dict__[2] = 3
"""


def test_built
