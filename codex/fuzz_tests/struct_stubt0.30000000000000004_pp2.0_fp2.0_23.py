from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a class method, so you can't call it on an instance.
# It's not really a constructor, it's a factory.

# The __new__() method is called before __init__()
# __new__() is responsible for returning a new instance of the class.
# __init__() is responsible for initializing the instance.

# __new__() is a static method.
# __init__() is an instance method.

# __new__() is called first, and is responsible for returning a new instance of your class.
# The __init__() method is called afterwards and can use the returned instance to set the attributes.

# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() doesn't return anything; it's only responsible for initializing the instance after it's been created.

# __new__() is a static method (special-cased so you need not declare it as such) that takes the class of
