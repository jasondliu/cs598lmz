from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is the constructor for the class.
# __init__() is the initializer for the object.

# __new__() is called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is not required to return anything; it's only responsible for initializing the instance after it's been created.
# In general, you shouldn't need to override __new__() unless you're subclassing an immutable type like str, int, unicode or tuple.

# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is the second step of instance creation. It's called last, and is responsible for initializing the instance after it's been created.
# In general, you shouldn't need to override __new__() unless you're subclassing an immutable type like str, int, unicode or tuple.

# __new__() is the first step of instance creation. It's called first, and is responsible for returning a
