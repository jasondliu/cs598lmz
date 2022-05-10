import types
types.MethodType(foo, None)

class C:
    def __getattribute__(self, name):
        if name == "foo":
            return 1
        else:
            return 2

C().foo

def foo(self, arg):
    return arg + 1

class C:
    pass

C.foo = types.MethodType(foo, None)

C().foo(1)

class C:
    pass

foo = types.MethodType(lambda self, arg: arg + 1, None, C)

C().foo(1)

class C:
    def __init__(self):
        self.foo = types.MethodType(lambda self: self, self)

C().foo()

class C:
    def __init__(self):
        self.foo = types.MethodType(lambda self: self, self, C)

C().foo()

class C:
    def __init__(self):
        self.foo = types.MethodType(lambda self: self, self, C)

c = C()
c.foo
