from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# __new__ is a static method, so it can be called on the class, not an instance
# __new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.

# __new__ is the method that's called when you call the class.
# __init__ is the method that's called when you call the instance.

# __new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.

# __new__ is the method that's called when you call the class.
# __init__ is the method that's called when you call the instance.

# __new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your
