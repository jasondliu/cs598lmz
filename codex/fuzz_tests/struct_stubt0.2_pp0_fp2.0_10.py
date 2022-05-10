from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method (special-cased so you needn't declare it as such) that takes the class of which an instance was requested as its first argument.
# It is called before __init__() and is expected to return an instance of that class.
# In our example, the default implementation of __new__() in object.__new__() simply creates the instance.
# We can override __new__() to customize instance creation, usually by taking additional arguments and passing them to the __init__() method of the class.
# For example, we can use __new__() to ensure that no instance with a negative size will be created:

class Structure2:
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
    def __repr__
