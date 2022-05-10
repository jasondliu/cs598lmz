fn = lambda: None
# Test fn.__code__
TestFunc2.fn.__code__ = type(None)
# Test class.__bases__
class TestFunc3:
    "Test Class 3"
    def __init__(self, fn):
        self.fn = fn
TestFunc3.__bases__ = (TestFunc1, TestFunc2)

# Test Python Function if needed
class TestFunc4:
    "Test Python Function"
    def __init__(self, fn):
        self.fn = fn
TestFunc4.fn.__code__ = TestFunc4.__init__.__func__.__code__
TestFunc4.fn.__name__ = 'PythonFunction'

def lambda1(n):
    return n % 10 == 1

def lambda2(n):
    return n % 10 == 2

def lambda3(n):
    return n % 10 == 3

def lambda4(n):
    return n % 10 == 4

def lambda5(n):
    return n % 10 == 5

def lambda6(n):
    return n
