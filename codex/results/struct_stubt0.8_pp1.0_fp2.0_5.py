from _struct import Struct
s = Struct.__new__(Struct)
print(s)
print(type(Struct))

# __new__ is called first. __new__ should return an instance, then the instance will have __init__ called.
# __new__ is the opposite of __del__, which gets called last.
# when a class is about to be instantiated, metaclass decides what class to instantiate.
# If a class defines __metaclass__, that's the metaclass that gets called.
# If __metaclass__ isn't set, but the class's base class is, the base class's metaclass is used.
# If neither of those is set, the default metaclass is type.


# When a metaclass is used,
# the magic is that the metaclass gets the chance to change what the class looked like.
# The metaclass can modify the class directly,
# or it can return a completely new class, which then gets assigned to the original name
# (so the original class is effectively replaced by the new one).


# In Python 3 you can leave out __metaclass__.
# The class definition has a built-in metac
