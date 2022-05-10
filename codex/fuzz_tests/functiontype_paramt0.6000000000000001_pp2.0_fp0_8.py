from types import FunctionType
list(FunctionType(lambda: None, globals())().__class__.__base__.__subclasses__())

[i.__name__ for i in list(FunctionType(lambda: None, globals())().__class__.__base__.__subclasses__())]

{i.__name__: i for i in list(FunctionType(lambda: None, globals())().__class__.__base__.__subclasses__())}

class A(object):
    def __init__(self):
        self.__class__.__base__.__subclasses__()

class B(A):
    def __init__(self):
        super(B, self).__init__()

class C(B):
    def __init__(self):
        super(C, self).__init__()

class D(C):
    def __init__(self):
        super(D, self).__init__()

D()

class E(C):
    def __init__(self):
        super(E, self).__init__()

E()
