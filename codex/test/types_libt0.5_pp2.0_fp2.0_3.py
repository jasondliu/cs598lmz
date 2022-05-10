import types
types.MethodType(foo, None)

def foo(self, *args, **kwargs):
    pass

class Bar(object):
    pass

types.MethodType(foo, Bar)

def foo(self, *args, **kwargs):
    pass

types.MethodType(foo, Bar)

def foo(self, *args, **kwargs):
    pass

class Bar(object):
    pass

types.MethodType(foo, Bar)

def foo(self, *args, **kwargs):
    pass

types.MethodType(foo, Bar)
