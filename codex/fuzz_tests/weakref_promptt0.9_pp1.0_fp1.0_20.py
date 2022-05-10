import weakref
# Test weakref.ref() on new-style object derived from object.
# Updated to use weakref.ref().

from test import test_support

derived = False

# base class:
class Str(str):
    pass

# derived class:
class Str_sub(object,Str):
    # just add something to Str to make the instanceobjects look different
    derived = True

def noop():
    pass

# derive from Str_sub:
class Str_sub_sub(object,Str_sub):
    pass

class Str_sub_sub_sub(object,Str_sub_sub):
    pass

class Str_sub_sub_sub_sub(Str_sub_sub_sub):
    pass

class Str_sub_sub_sub_sub_sub(Str_sub_sub_sub_sub):
    pass

# real derived class, with multiple inheritance
class MyStr(object,Str):
    def __repr__(self):
        return "MyStr: %s" % super(MyStr, self).__repr__()

class MyStr_sub(MyStr
