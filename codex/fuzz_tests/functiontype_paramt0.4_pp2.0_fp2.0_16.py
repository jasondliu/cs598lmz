from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo') for x in range(10))

# Test that the "self" argument is passed to the __new__ method.
class A(object):
    def __new__(self, *args):
        return object.__new__(self)

class B(A):
    def __init__(self, *args):
        self.args = args

B(1, 2, 3)

# Test that the "self" argument is passed to the __init__ method.
class C(object):
    def __init__(self, *args):
        self.args = args

class D(C):
    def __new__(self, *args):
        return object.__new__(self)

D(1, 2, 3)

# Test that the "self" argument is passed to the __del__ method.
class E(object):
    def __del__(self):
        self.x = 1

E()

# Test that the "self" argument is passed to the __setattr__ method.
class F(
