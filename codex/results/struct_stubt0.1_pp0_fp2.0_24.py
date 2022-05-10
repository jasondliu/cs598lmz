from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called on the class, not on an instance.
# It is called before __init__() and is passed the class itself as the first argument.
# It's main purpose is to return a new instance of that class.
# In this case, it returns an instance of Struct, which is then initialized by __init__().

# __new__() is also called when subclassing an immutable type like str, int, unicode or tuple.
# It is the correct place to customize instance creation.
# For example, here is a subclass of str that returns uppercase strings:

class UpperStr(str):
    def __new__(cls, string):
        return str.__new__(cls, string.upper())

a = UpperStr('hello')
print(a)

# __new__() is also the correct place to do things like range checking on arguments.
# For example, here is a subclass of int that only allows values from 0 to 255:

class Int(int):
    def __
