from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance of the class.
# It is called before __init__() and is responsible for returning a new instance of your class.
# In the example above, __new__() is called on the class itself, so the first argument to __new__() is the class.
# The remaining arguments are the same as those passed to __init__().
# The return value of __new__() is the new object instance (self).
# In our example, we create a new instance of the class and then initialize it by calling __init__().
# If you override __new__(), you still need to call __init__() to initialize the object.
# If you don't, the object will be in an uninitialized state.

# The primary use of overriding __new__() is for subclassing immutable types like int, str, and tuple.
# Immutable types can't be changed.
# For example, you can't add items to a tuple.
# If you try, you get a new tuple instead.
# This is because
