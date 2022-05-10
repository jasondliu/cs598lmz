from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("I")
s.size

# __new__() is a class method that is called when the class is instantiated.
# The return value is the instance.
# __init__() is an instance method that is called after the instance is created.

# __new__() is called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is called last and is responsible for initializing the instance.

# The reason that __new__() exists is because sometimes you want to control the creation of a new instance.
# This is especially true when you want to control the memory management of the instance.

# In Python, you can override the default behavior for instantiating an object by defining the __new__() method.

# The __new__() method is a static method (special-cased so you need not declare it as such) that takes the class of which an instance was requested as its first argument.
# The remaining arguments are those passed to the object constructor expression (the call to the class).
# The __new__() method is intended mainly to allow subclasses of immutable types
