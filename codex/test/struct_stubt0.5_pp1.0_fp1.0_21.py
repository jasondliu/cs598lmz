from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I', 'data')
s.pack(1)

# in Python 3.5+, you need to use a different approach
# https://docs.python.org/3.5/library/struct.html#struct.Struct.__new__
s = Struct(">I")
s.pack(1)

# in Python 3.5+, you can also use a string as the format
s = Struct(">I")
s.pack(1)
