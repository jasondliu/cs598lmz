from types import FunctionType
list(FunctionType(code, globals()))

# Returns a generator
def outer():
    return (i for i in range(5))

list(outer())

# Returns a generator
def outer():
    def inner():
        return range(5)
    return inner()

list(outer())
