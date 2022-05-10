import ctypes
ctypes.cast(10, ctypes.py_object)

# test if object is an instance of a built-in type
isinstance(obj, int)

# test if object is an instance of a user-defined type
isinstance(obj, SomeClass)

# test if object is an instance of any class in a tuple of classes
isinstance(obj, (class1, class2, class3))

# test if object is an instance of a user-defined class
isinstance(obj, SomeClass)

# get the type of an object
type(obj)

# get the type of an object as a string
type(obj).__name__

# get the type of an object as a string
str(type(obj))

# get the type of an object as a type object
type(obj)

# get the type of an object as a class
obj.__class__

# get the type of an object as a class
type(obj)

# test if object is an instance of a built-in type
isinstance(obj, int)

# test if object is an instance of a user-
