from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(10))

# Test that the function name is not leaked to the outer scope.
def f():
    def g():
        pass
    assert g.__name__ == 'g'
    return g
assert f().__name__ == 'g'

# Test that the function name is not leaked to the outer scope.
def f():
    def g():
        pass
    assert g.__name__ == 'g'
    return g
assert f().__name__ == 'g'

# Test that the function name is not leaked to the outer scope.
def f():
    def g():
        pass
    assert g.__name__ == 'g'
    return g
assert f().__name__ == 'g'

# Test that the function name is not leaked to the outer scope.
def f():
    def g():
        pass
    assert g.__name__ == 'g'
    return g
assert f().__name__ == 'g'

# Test that the function name is not leaked to the outer scope.
def
