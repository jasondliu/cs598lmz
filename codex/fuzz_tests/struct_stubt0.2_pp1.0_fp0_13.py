from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, and is called before __init__()
# __new__() is responsible for returning a new instance of your class
# __init__() is responsible for initializing the instance
# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is called last, and is responsible for initializing the instance.
# __new__() is called first, allowing it to control the creation of new instances
# __init__() is very commonly overridden in classes, and is often what you think of as the class constructor
# __new__() is rarely overridden, and is often ignored altogether
# __new__() is the actual constructor
# __init__() is the initializer
# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is called last, and is responsible for initializing the instance.
# __new__() is
