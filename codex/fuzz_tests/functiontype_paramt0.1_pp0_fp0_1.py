from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(10))

# Test that we can create a function with a closure that has a cell with a
# function as a value.
def f():
    def g():
        return 1
    return g

def h():
    return f()

h()()

# Test that we can create a function with a closure that has a cell with a
# function as a value, and that the function has a closure.
def f():
    def g():
        def h():
            return 1
        return h
    return g

def i():
    return f()

i()()()

# Test that we can create a function with a closure that has a cell with a
# function as a value, and that the function has a closure that has a cell with
# a function as a value.
def f():
    def g():
        def h():
            def i():
                return 1
            return i
        return h
    return g

def j():
    return f()

j()()()()

# Test that we
