import types
types.MethodType(lambda self: None, None, None)

# classes
class A(object):
    def __init__(self):
        pass

class B(A):
    def __init__(self):
        pass

class C(A):
    def __init__(self):
        pass

class D(B, C):
    def __init__(self):
        pass

class E(object):
    def __init__(self):
        pass

