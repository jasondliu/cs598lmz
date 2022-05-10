from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called on the class, not on an instance.
# It is called before __init__() and is passed the class itself as the first argument.
# It is also passed any arguments passed to the class constructor expression.
# The return value of __new__() is the new object instance (usually an instance of its class).
# If __new__() does not return an object of the type it is supposed to create,
# the class constructor will raise a TypeError exception.

# __init__() is a regular instance method and is called after the instance has been created.
# It is passed the new object instance as its first argument,
# and any arguments passed to the class constructor expression are passed as subsequent arguments.
# The return value of __init__() does not matter; it is always ignored.

# __new__() is the first step of instance creation. It's called first,
# and is responsible for returning a new instance of your class.
# In contrast, __init__() doesn't return anything; it's only responsible for
