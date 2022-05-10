import types
types.MethodType(lambda self: None, None, None)

# ___________________________________________________________________________
# Classes

class A(object):
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.y = 2

class C(A):
    def __init__(self):
        super(C, self).__init__()
        self.z = 3

class D(B, C):
    def __init__(self):
        super(D, self).__init__()
        self.z = 4

class E(D):
    def __init__(self):
        super(E, self).__init__()
        self.z = 5

class F(E):
    def __init__(self):
        super(F, self).__init__()
        self.z = 6

class G(F):
    def __init__(self):
        super(G, self).__init__()
        self.z
