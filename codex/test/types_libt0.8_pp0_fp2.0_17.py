import types
types.SimpleNamespace(**{'__qualname__': 'c.1', 'x': 0})
types.SimpleNamespace(__qualname__='c.1', x=0)
p = types.SimpleNamespace(__qualname__='c.1', x=0)
d = p.__dict__
d['x'] = 42
p
p.x = 0

# bpo-33221: __qualname__ of a function defined in exec()
def test_function_qualname_in_exec():
    glob = {}
    loc = {}
    exec("""
def f():
   pass
""", glob, loc)
    assert loc['f'].__qualname__ == 'f'

    exec("""
def f():
   pass
f.__qualname__ = 'g'
""", glob, loc)
    assert loc['f'].__qualname__ == 'g'
    assert repr(loc['f']) == "<function f at 0x%x>" % id(loc['f'])

