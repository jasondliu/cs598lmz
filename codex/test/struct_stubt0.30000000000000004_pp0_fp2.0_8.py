from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# __new__ is a class method, so it is called on the class itself
# __init__ is an instance method, so it is called on the instance
# __new__ is called before __init__
# __new__ is responsible for returning an instance of the class
# __init__ is responsible for initializing the instance
# __new__ can return any object, not just an instance of the class
# if __new__ returns an instance of the class, then __init__ will be called on that instance
# if __new__ returns any other object, then __init__ will not be called

# __new__ is called when the class is ready to instantiate itself
# __init__ is called when the instance is ready to initialize itself

# __new__ is the first step of instance creation
# it's called first, and is responsible for returning a new instance of your class
# in contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created

# __new__ is called first, and is responsible for returning a new
