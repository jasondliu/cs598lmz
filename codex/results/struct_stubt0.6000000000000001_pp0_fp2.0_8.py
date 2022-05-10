from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class. In contrast, __init__() is called after __new__(), and is responsible for initializing the instance.
# The problem with __init__() is that you can't use it to return a value other than None.
# So if you want to customize the creation of a new instance, you have to override __new__(). 

# For example, here's a simple class that lets you add attributes to an instance at creation time:
class Structure:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

# Example class definitions

if __name__ == '__main__':

