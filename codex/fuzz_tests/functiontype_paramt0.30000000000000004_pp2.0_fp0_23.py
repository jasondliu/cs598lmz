from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(10))

# This is a test for the new '__qualname__' attribute.
# It should be the same as '__name__' for functions defined at the top level
# of a module.
def f():
    pass

def g():
    pass

def h():
    pass

class C:
    def f():
        pass

    def g():
        pass

    def h():
        pass

def f():
    pass

def g():
    pass

def h():
    pass

class C:
    def f():
        pass

    def g():
        pass

    def h():
        pass

def f():
    pass

def g():
    pass

def h():
    pass

class C:
    def f():
        pass

    def g():
        pass

    def h():
        pass

def f():
    pass

def g():
    pass

def h():
    pass

class C:
    def f():
       
