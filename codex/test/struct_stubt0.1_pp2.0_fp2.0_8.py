from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# __new__ is a class method, so it is called on the class, not on an instance.
# It is called before __init__, and it is the method that creates the instance.
# It is called with the class as the first argument, and the arguments that
# were passed to the class constructor as the rest of the arguments.
# It should return the new instance.
# If it returns an instance of cls, then the new instance’s __init__() method
# will be invoked like __init__(self[, ...]), where self is the new instance
# and the remaining arguments are the same as were passed to __new__().
# If it returns any other value, then the new instance’s __init__() method
# will not be invoked.

# __init__ is an instance method, so it is called on the instance, not on the
# class. It is called after __new__, and it is the method that initializes the
# instance. It is called with the instance as the first argument, and the
# arguments that were
