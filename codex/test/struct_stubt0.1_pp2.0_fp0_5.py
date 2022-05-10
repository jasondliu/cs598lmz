from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it doesn't need an instance of the class
# to be called.

# __new__() is called before __init__()
# __new__() is responsible for returning a new instance of the class.
# __init__() initializes the new instance.

# __new__() is the first step of instance creation. It's called first, and is
# responsible for returning a new instance of your class. In contrast,
# __init__() doesn't return anything; it's only responsible for initializing
# the instance after it's been created.

# __new__() is a static method (special-cased so you needn't declare it as such)
# that takes the class of which an instance was requested as its first argument.
# The remaining arguments are those passed to the object constructor expression
# (the call to the class).
# The return value of __new__() should be the new object instance (usually an
# instance of cls).

# __init__() is a plain instance method. Its first
