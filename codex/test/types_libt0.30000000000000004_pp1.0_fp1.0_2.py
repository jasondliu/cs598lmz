import types
types.MethodType(lambda self: None, None, None)

# The following should not crash
def f():
    class C:
        def __init__(self):
            self.x = 1
        def __getattr__(self, name):
            return self.x
    c = C()
    c.y = 2
    c.z = 3
    return c.y + c.z

assert f() == 5

def f():
    class C:
        def __getattr__(self, name):
            return 1
        def __setattr__(self, name, value):
            pass
    c = C()
    c.y = 2
    c.z = 3
    return c.y + c.z

assert f() == 5

def f():
    class C:
        def __getattr__(self, name):
            return 1
        def __setattr__(self, name, value):
            pass
        def __delattr__(self, name):
            pass
    c = C()
    c.y = 2
