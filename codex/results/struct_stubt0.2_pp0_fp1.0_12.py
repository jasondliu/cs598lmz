from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method, so it is called without an instance of the class.
# It returns a new instance of the class.
# __init__ is an instance method, so it is called with an instance of the class.
# It initializes the instance.

# __new__ is called first, and is responsible for returning a new instance of your class.
# In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.

# The only time you need to implement __new__ is when you need to control the creation of a new instance.
# Implementing __new__ is a bit tricky because you have to follow the protocol of returning a new instance of the class.
# If you don't do this, you will not get the benefits of the new style class.

# __new__ is a static method (special-cased so you need not declare it as such) that takes the class of which an instance was requested as its first argument.
# The remaining arguments are those passed to the object constructor expression (the call to
