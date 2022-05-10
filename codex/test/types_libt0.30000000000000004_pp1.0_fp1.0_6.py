import types
types.ModuleType.__getattr__ = lambda self, name: self.__dict__[name]

# Import the module
import example

# Check the result
assert example.add(1, 2) == 3

# Check the result
assert example.sub(1, 2) == -1

# Check the result
assert example.mul(1, 2) == 2

# Check the result
assert example.div(1, 2) == 0.5

# Check the result
assert example.mod(1, 2) == 1

# Check the result
assert example.pow(1, 2) == 1

# Check the result
assert example.iadd(1, 2) == 3

# Check the result
assert example.isub(1, 2) == -1

# Check the result
assert example.imul(1, 2) == 2

# Check the result
assert example.idiv(1, 2) == 0.5

