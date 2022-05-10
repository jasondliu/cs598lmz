from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('')

# New notation
s = Struct()
s.__init__('i')
s = Struct('i')

# Classical notation (to be used in most cases)
s = Struct('i')

# We can use the result of __new__ directly (of course without passing argument)
s.__new__(Struct)

# __call__ is callable too !
s.__call__('i')

# We can still use the classical notation
s('i')
