from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called on the class, not on an instance.
# It is called before __init__()
# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is only called after __new__() has finished its job.
# __new__() is the method that creates an instance of a class. It is called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is only called after __new__() has finished.
# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is only called after __new__() has finished its job.
# __new__() is the method that creates an instance of a class. It is called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is only called after
