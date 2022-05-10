from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# __new__ is a static method (special-cased so you needn't use @staticmethod)
# that takes the class as its first argument
s = Struct.__new__(Struct, 'I 2s f')
s.size

# When the class is created, the __init__ method is called with the arguments
# that were passed to the class constructor expression

# After that the instance is returned to the caller
# There is no need to explicitly return the instance reference as the last
# value in the __init__ method: doing so would just result in the original
# reference being explicitly returned, which is pointless

# When implementing a class, the __init__ method may find it useful to consult
# the class documentation, which can be obtained as __doc__ on the class object

# The class documentation will usually contain information about the
# constructor arguments, so it can be displayed to users along with
# argument parsing errors

# The class documentation is also used by tools such as the pydoc help system
# and the built-in help function

#
