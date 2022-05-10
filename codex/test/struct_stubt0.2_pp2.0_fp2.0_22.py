from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# __new__ is a class method, so you can't call it on an instance.
# You can call it on the class, but that's not what you want.
# You want to call __init__, which is an instance method.
# So you have to create an instance first.

# The __new__ method is called when you create a new instance.
# It's responsible for creating the instance and returning it.
# The __init__ method is called when you have an instance,
# and you want to initialize it.

# The __new__ method is called when you create a new instance.
# It's responsible for creating the instance and returning it.
# The __init__ method is called when you have an instance,
# and you want to initialize it.

# The __new__ method is called when you create a new instance.
# It's responsible for creating the instance and returning it.
# The __init__ method is called when you have an instance,
# and you want to initialize it.

# The __new__ method is called when
