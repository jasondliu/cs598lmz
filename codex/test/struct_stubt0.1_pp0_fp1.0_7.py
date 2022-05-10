from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance.
# It is called before __init__() and is responsible for returning a new instance of your class.
# In contrast, __init__() is a regular instance method and is called after __new__().
# The __init__() method is where you do most of your initialization work.

# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() doesn't return anything; it's only responsible for initializing the instance after it's been created.

# In general, you shouldn't need to override __new__() unless you're subclassing an immutable type like str, int, unicode or tuple.

# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() doesn't return anything; it's only responsible for initializing the instance after it's been created.

# In
