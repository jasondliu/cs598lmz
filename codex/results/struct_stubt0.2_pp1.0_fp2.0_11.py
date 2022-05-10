from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance.
# The first argument is the class to be instantiated.
# The remaining arguments are passed to __init__()

# __new__() is called before __init__()
# __new__() returns the new instance, while __init__() returns None

# __new__() is the first step of instance creation.
# It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() doesn't return anything; it's only responsible for initializing the instance after it's been created.

# __new__() is called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() doesn't return anything; it's only responsible for initializing the instance after it's been created.

# __new__() is the first step of instance creation.
# It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() doesn't return anything; it's
