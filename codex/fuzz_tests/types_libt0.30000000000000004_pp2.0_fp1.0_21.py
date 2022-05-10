import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

class A(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class B(A):
    def __init__(self, name):
        super(B, self).__init__(name)

class C(A):
    def __init__(self, name):
        super(C, self).__init__(name)

class D(B, C):
    def __init__(self, name):
        super(D, self).__init__(name)

print(D('d'))

class A(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class B(A):
    def __init__(self, name):
        super(B, self).__init__(name)

class C(A):
    def __init__(
