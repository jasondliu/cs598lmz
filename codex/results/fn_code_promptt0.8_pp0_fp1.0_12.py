fn = lambda: None
# Test fn.__code__
print("fn.__code__", fn.__code__)
# Lookup __code__ attribute on fn
print("fn.__dict__['__code__']", fn.__dict__['__code__'])

# Create a new function
def add(x: int, y: int) -> int:
    return x + y

# Get the code object
print("add.__code__", add.__code__)

# Disassemble the code object
import dis
dis.dis(add.__code__)

# Infer the annotations
print("add.__annotations__", add.__annotations__)
# Use the annotations
help(add)

# Define a function to show the effect of annotations
def add(x: int, y: 'adds x to y') -> int:
    return x + y

# Get the annotations
print("add.__annotations__", add.__annotations__)
# Use the annotations
help(add)

# Define a function with default arguments
def add(x: int, y: int = 1) -> int
