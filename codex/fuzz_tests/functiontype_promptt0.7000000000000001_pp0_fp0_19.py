import types
# Test types.FunctionType (and types.LambdaType)

class A:
    def __init__(self, value):
        self.value = value
    def m1(self):
        pass

class B:
    def __init__(self, value):
        self.value = value
    def __call__(self):
        pass

def m2(self):
    pass

class C:
    def __init__(self, value):
        self.value = value
    m2 = m2

class D:
    def __init__(self, value):
        self.value = value
    @staticmethod
    def m3():
        pass

class E(A):
    def m4(self):
        pass

class F(A):
    m4 = m2

class G(A):
    @staticmethod
    def m5():
        pass

class H(A):
    m5 = m2

def f():
    pass

g = lambda: None

def test_function_type():
    assert type(A.__
