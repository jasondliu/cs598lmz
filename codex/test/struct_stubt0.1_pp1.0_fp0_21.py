from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a class method, so it is called on the class, not on an instance.
# The first argument to __new__ is the class that is being constructed.
# The remaining arguments are the same as those passed to __init__.
# __new__ must return an instance of the class.
# If it does not, the class construction will fail.
# If __new__ returns an instance of a subclass, the instance returned by __init__ will be that subclass.
# If __new__ returns an instance of the class, the instance returned by __init__ will be that instance.
# If __new__ does not return an instance of the class or of a subclass, the class construction will fail.
# If __new__ does not return an instance of the class or of a subclass, the class construction will fail.
# If __new__ does not return an instance of the class or of a subclass, the class construction will fail.
# If __new__ does not return an instance of the class or of a subclass, the class construction will fail.
# If __new__ does not return
