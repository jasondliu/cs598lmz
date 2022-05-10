import types
types.MethodType(test, None, None)

class A(object):
    def __init__(self):
        self.x = 'A'

a = A()

class B(object):
    def __init__(self):
        self.x = 'B'

b = B()

