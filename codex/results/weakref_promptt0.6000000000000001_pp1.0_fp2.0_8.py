import weakref
# Test weakref.ref
#
# Note that weakref.ref() doesn't really work with old-style classes
# (the __weakref__ attribute is not set).

class C: pass

class C_new(object): pass

class C_new_kwargs(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class D:
    def __init__(self, obj):
        self.obj = obj

    def __call__(self):
        return self.obj

class E:
    def __init__(self, obj):
        self.obj = obj

    def __call__(self):
        return 42

class F:
    def __init__(self, obj):
        self.obj = obj

    def __call__(self):
        raise ValueError

class G:
    def __init__(self, obj):
        self.obj = obj

    def __call__(self):
        return self

def check(a, b):
    if a is not b:
        raise Test
