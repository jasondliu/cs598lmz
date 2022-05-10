import types
types.IntType
# Output: <type 'int'>

"""

"""
It is easy to get the type of variable in Python. You can simply use the type() function to get the type.

>>> a = 5
>>> type(a)
<type 'int'>
>>> a = 2.0
>>> type(a)
<type 'float'>
>>> a = 1+2j
>>> type(a)
<type 'complex'>
>>> a = 'hello world'
>>> type(a)
<type 'str'>

"""

"""
Python Numbers
Python supports integers, floating point numbers and complex numbers. They are defined as int, float and complex class in Python.

We can use the type() function to know which class a variable or a value belongs to and the isinstance() function to check if an object belongs to a particular class.

>>> a = 5
>>> isinstance(a, int)
True
>>> a = 5.0
>>> isinstance(a, int)
False
>>> isinstance(a, float)
True

"""

"""
We can represent integers using a few different notations.
