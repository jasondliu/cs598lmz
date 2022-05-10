import ctypes
ctypes.cast(0, ctypes.py_object)

# ______________________________________________________________________________

# A class can implement certain operations that are invoked by special syntax
# (such as arithmetic operations or subscripting and slicing) by defining
# methods with special names. This is Python's approach to operator overloading,
# allowing classes to define their own behavior with respect to language
# operators. For example, if a class defines a method named __getitem__,
# and x is an instance of this class, then x[i] is roughly equivalent to
# type(x).__getitem__(x, i). Except where mentioned, attempts to execute an
# operation raise an exception when no appropriate method is defined (typically
# AttributeError or TypeError).

# The following methods can be defined to implement sequence behavior.
# The in and not in operations are defined to have the same priorities as ==
# and !=, and evaluted from left to right.

# __len__(self)
# Return the length (the number of items) of an object. The argument may be a
# sequence (such as a string, bytes, tuple, list, or range) or a collection
