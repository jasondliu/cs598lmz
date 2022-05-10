from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance of the class.
# It is called before __init__()
# __new__() is responsible for returning a new instance of the class.
# __init__() is responsible for initializing the instance.
# __new__() is called first, so it is responsible for creating the instance.
# __init__() is called second, so it is responsible for initializing the instance.
# __new__() can return any object, while __init__() must return None.
# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# The __init__() method is called last. It's used to initialize the instance object.
# __new__() is called first, so it is responsible for creating the instance.
# __init__() is called second, so it is responsible for initializing the instance.
# __new__() can return any object, while __init__() must return None.
# __new__() is the
