from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called on the class, not on an instance.
# It is called before __init__() and is passed the class itself.
# It is used to return a new instance of the class.
# It is usually overridden to customize the instance creation process.
# It can also be used to return a new instance of a subclass.

# __init__() is a regular method, so it is called on an instance.
# It is called after __new__() and is passed the instance.
# It is used to initialize the instance.
# It is usually overridden to customize the instance initialization process.

# __new__() is called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is called last and is responsible for initializing the instance.
# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is the second step of instance creation. It's called last
