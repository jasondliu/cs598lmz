from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(10))

# Test that the function name is not leaked to the outer scope.
def f():
    def g():
        pass
    return g

f()

# Test that the function name is not leaked to the outer scope.
def f():
    def g():
        pass
    return g

f()

# Test that the function name is not leaked to the outer scope.
def f():
    def g():
        pass
    return g

f()

# Test that the function name is not leaked to the outer scope.
def f():
    def g():
        pass
    return g

f()

# Test that the function name is not leaked to the outer scope.
def f():
    def g():
        pass
    return g

f()

# Test that the function name is not leaked to the outer scope.
def f():
    def g():
        pass
    return g

f()

# Test that the function name is not leaked to the outer scope.
def f():
   
