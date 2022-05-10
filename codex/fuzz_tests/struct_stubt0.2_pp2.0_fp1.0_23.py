from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased by the interpreter)
# __init__ is a regular instance method

# When we call a class, it's __new__ method is invoked first
# to create an empty object, then the __init__ method is invoked
# to initialize the instance.

# __new__ is the first step of instance creation. It's called first,
# and is responsible for returning a new instance of your class.
# In contrast, __init__ doesn't return anything; it's only responsible
# for initializing the instance after it's been created.

# In general, you shouldn't need to override __new__ unless you're
# subclassing an immutable type like str, int, unicode or tuple.

# The __init__ method for a class is implicitly passed the new instance
# as its first argument, which by convention is called self.

# The __init__ method is run as soon as an object of a class is instantiated.
# The method is useful to do any initialization you want to do with your object.

#
