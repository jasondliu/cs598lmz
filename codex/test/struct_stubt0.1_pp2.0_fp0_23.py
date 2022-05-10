from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method (special-cased so you needn't declare it as such) that takes the class of which an instance was requested as its first argument.
# It is called before __init__() and is expected to return an instance of that class.
# In the example, the return value of object.__new__() is not used.
# This is typical for classes that override __init__(); they return the new instance in __init__() by assigning to self.

# The __init__() method may be documented in either the class level docstring, or as a docstring on the __init__ method itself.
# If the latter is chosen, it should be triple-quoted so that it extends over more than one line,
# unless it is very short.
# If the class has public attributes, they may be documented here in an __attributes__ section and follow the same formatting as a function’s __variables__ section.

# The __init__() method should minimize the side effects of the instance creation and initialization,
# and should not do anything
