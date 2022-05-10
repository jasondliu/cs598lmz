import types
types.new_class('X', (object,), {})

# This should not crash
import pydoc
pydoc.help(X)


# This should not crash
def f():
    class C(object):
        def __init__(self):
            self.foo = 1
            self.bar = 2
    c = C()
    return c.foo, c.bar


