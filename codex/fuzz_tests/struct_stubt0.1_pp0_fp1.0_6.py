from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called on the class, not on an instance.
# It is called before __init__()
# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is only called after __new__() has finished.
# __new__() is the method that creates an instance of your class, and then passes it as an argument to __init__().
# __init__() is the method that initializes the instance.
# __new__() is called first, so it can modify the arguments passed to __init__() or even prevent __init__() from being called at all.
# __new__() is the method that's called when you call the class.
# __init__() is the method that's called when you call the instance.
# __new__() is the method that's called when you call the class.
# __init__() is the method that's called when you call the instance.
# __new__
