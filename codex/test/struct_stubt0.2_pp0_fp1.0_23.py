from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# __new__ is a class method, so it's called on the class, not on an instance.
# __new__ is called before __init__, and is responsible for returning a new instance of your class.
# In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.
# __new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.
# In general, you shouldn't need to override __new__ unless you're subclassing an immutable type like str, int, unicode or tuple.

# __new__ is a static method (special-cased so you need not declare it as such) that takes the class of which an instance was requested as its first argument.
# The remaining arguments are those passed to the object constructor expression (the call to the class).
# The return value of __new__ should be the new object
