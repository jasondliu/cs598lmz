from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__).__closure__)

# Create a closure
def adder(x):
    def add(y):
        return x + y
    return add

adder(1)(2)

# A closure is a function with an extended scope that encompasses nonglobal variables referenced in the body of the function but not defined there. It does not matter whether the function is anonymous or not; what matters is that it can access nonglobal variables that are defined outside of its body.

# When you call adder(1), you’re telling Python to execute the adder function with x set to 1. Python executes the function body and sees that it contains a nested function, add, so it creates a function object for add, as usual. However, the function object for add has an extended scope with a reference to x, which is in the enclosing scope.

# You can see this by inspecting the __closure__ attribute of the returned add function. It contains a cell object containing a reference to the x variable.


