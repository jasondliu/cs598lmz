from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it can be called on the class itself.
# It is called before __init__() and is used to return a new instance of the class.
# It is also used to change the signature of the constructor.
# For example, the following code creates a new class that has an additional argument.
# This argument is used to set the value of the new instance.

class NewInit(object):
    def __new__(cls, *args, **kwargs):
        print('__new__ called')
        return super(NewInit, cls).__new__(cls, *args, **kwargs)

    def __init__(self, value):
        print('__init__ called')
        self.value = value

# Create an instance of the class.
# The __new__() method is called first.
# It is followed by __init__().
# The __new__() method is responsible for returning a new instance of the class.
# The __init__() method is responsible for initializing the
