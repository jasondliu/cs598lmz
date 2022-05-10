import types
types.MethodType(foo, None, None)

# http://bugs.python.org/issue1202
class A(object):
    def __init__(self):
        self.foo = 1

a = A()
a.foo = 2

# http://bugs.python.org/issue1203
class A(object):
    def __init__(self):
        self.foo = 1

a = A()
a.foo = 2

# http://bugs.python.org/issue1204
class A(object):
    def __init__(self):
        self.foo = 1

a = A()
a.foo = 2

# http://bugs.python.org/issue1205
class A(object):
    def __init__(self):
        self.foo = 1

a = A()
a.foo = 2

# http://bugs.python.org/issue1206
class A(object):
    def __init__(self):
        self.foo = 1

a = A()
a.foo = 2

# http://bugs
