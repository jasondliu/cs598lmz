from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is called to create the object, __init__() is called to initialize it.

# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class. In contrast, __init__() doesn't return anything; it's only responsible for initializing the instance after it's been created.

# In general, you shouldn't need to override __new__() unless you're subclassing an immutable type like str, int, unicode or tuple.

# __init__() is the second step of instance creation. It's called after __new__(), and is responsible for initializing the instance.

# __init__() is the most commonly used method for object initialization.

# __new__() is called first, and is responsible for returning a new instance of your class. In contrast, __init__() doesn't return anything; it's only responsible for initializing the instance after it's been created.

# In general, you shouldn't need to override __new__() unless you're subclassing an immutable type like str
