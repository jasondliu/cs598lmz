from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance.
# It is called before __init__()
# __new__() returns an instance, which is then passed to __init__()

# __new__() is used to control instance creation
# __init__() is used to control initialization of the instance

# __new__() is the first step of instance creation.
# It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() doesn't return anything; it's only responsible for initializing the instance after it's been created.

# In general, you shouldn't need to override __new__() unless you're subclassing an immutable type like str, int, unicode or tuple.

# __new__() is called before __init__()
# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() doesn't return anything; it's only responsible for initializing the instance after
