import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

class A(object):
    def __init__(self):
        self.name = 'A'

class B(object):
    def __init__(self):
        self.name = 'B'

class C(object):
    def __init__(self):
        self.name = 'C'

class D(object):
    def __init__(self):
        self.name = 'D'

class E(object):
    def __init__(self):
        self.name = 'E'

class F(object):
    def __init__(self):
        self.name = 'F'

class G(object):
    def __init__(self):
        self.name = 'G'

