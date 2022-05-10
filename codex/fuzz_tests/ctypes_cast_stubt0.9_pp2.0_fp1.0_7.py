import ctypes
ctypes.cast(ptr, ctypes.c_size_t)

You can use a ctypes pointer in any way a regular pointer would be used, including passing it to C code. Actually, since the ctypes.c_void_p type is a subclass of ctypes.c_char_p, you can do anything with a ctypes pointer that you could do with a regular char* pointer, such as indexing it or treating it as an array. 

The Python 'class' statement creates a new type of class, a type of object, referred to in the Python documentation as a "new-style class". A new-style class has a different definition than an old-style one. It has object-oriented features that have never existed in any Python class prior to its introduction in Python version 2.2.

The syntax of the class statement itself is notably different in Python 2.2+ different from the older style of the Python class definition:

class AClass(BaseClass0, BaseClass1, ...):
    ...
The argument(s) following the class name in parentheses define the base class(es). One or more may be specified. All arguments that follow the class name will be bases
