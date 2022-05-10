import types
types.ClassType

# Check if an object is a type
# It'll be true for an actual type as well as an instance of that type
p = Person()
isinstance(int, type) # True
isinstance(type, type) # True
isinstance(None, NoneType) # ValueError: isinstance() arg 2 must be a type or tuple of types
isinstance(None, type) # True
isinstance(p, type) # False
