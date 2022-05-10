from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# __new__ is a class method
# __init__ is an instance method

# __new__ is called before __init__
# __new__ returns the instance
# __init__ initializes the instance

# __new__ is called when an instance of the class is needed
# __init__ is called when the instance is returned by __new__

# __new__ is the first step of instance creation
# It's called first, and is responsible for returning a new instance of your class
# In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created

# __new__ is a static method (special-cased so you needn't declare it as such)
# __init__ is a normal instance method

# __new__ is the method called before __init__
# __new__ is the first step in instance creation
# It can be overridden to customize instance creation
# It's the opposite of __del__ which is the last step in instance destruction

# __new__ is the method called before
