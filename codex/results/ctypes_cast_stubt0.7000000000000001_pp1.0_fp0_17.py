import ctypes
ctypes.cast(0, ctypes.py_object).value

# None is the one and only instance of this type. There is a singleton None object.
# Because None is an object, we cannot use == to compare objects to see if they are None. 
# Use is instead.
a = None
print(a is None)

# Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below. 
# The following values are considered false: 
# None, numeric zero of all types, and empty strings and containers (including strings, tuples, lists, dictionaries, sets and frozensets).
# All other values are considered true.
a = 5
if a:
    print("foo")

# is operator: object identity - Returns True if both variables are the same object.
a = [1, 2, 3]
b = a
print(a == b)
print(a is b)

# The is operator tests for object identity. 
# This isn’t the same as equality, although a and b contain the same content.
# The == operator tests
