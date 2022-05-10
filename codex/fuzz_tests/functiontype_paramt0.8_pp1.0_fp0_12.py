from types import FunctionType
list(FunctionType(lambda x: x + 1, (), {}, None) for x in range(4))

"""
As a remark, this kind of manipulation should never be done in real life, 
resorting to real closures being much better. However, it may have some 
academic interest.

This is probably a good time to start discussing the Py3.3 implementation, 
which starts from a different base, that is, from the concept of cell.
"""

"""
A cell object is an object which stores the link between a free variable in a 
nested function and its value. A nested function references a free variable 
if it is defined in a non-global scope and if its value is set by a non-global 
scope. A cell stores the details of this relationship.

The rationale behind cell objects is to enable the implementation of nested 
functions, which are functions defined in non-global scopes.
"""

"""
One interesting characteristic of cell objects is that they can be serialized 
and deserialized using the pickle module. They are also defined in their own 
class, called cell.

In the source code, the
