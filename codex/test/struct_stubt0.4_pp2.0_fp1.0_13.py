from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# __new__ is a static method
# __init__ is an instance method

# __new__ is called first
# __init__ is called second

# __new__ returns an instance of the class
# __init__ returns None

# __new__ can return any object
# __init__ can only return None

# __new__ can accept additional arguments
# __init__ cannot accept additional arguments

# __new__ is the first step of instance creation
# __init__ is the second step of instance creation

# __new__ is called only once
# __init__ can be called multiple times

# __new__ is the constructor
# __init__ is the initializer

# __new__ can be overridden in derived classes
# __init__ cannot be overridden in derived classes

# __new__ can be called from within Python code
# __init__ cannot be called from within Python code

# __new__ can be called from C code
# __init__ cannot be called from C code

# __new__ is the first step
