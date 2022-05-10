from types import FunctionType
list(FunctionType(lambda: None, globals()) for _ in range(10))

class A:
    def f(self):
        pass

list(A().f for _ in range(10))

list(range(10))

def f():
    for _ in range(10):
        yield

list(f())

list(FunctionType(lambda: None, globals()) for _ in range(10))

class A:
    def f(self):
        pass

list(A().f for _ in range(10))

list(range(10))

def f():
    for _ in range(10):
        yield

list(f())

list(FunctionType(lambda: None, globals()) for _ in range(10))

class A:
    def f(self):
        pass

list(A().f for _ in range(10))

list(range(10))

def f():
    for _ in range(10):
        yield

list(f())
