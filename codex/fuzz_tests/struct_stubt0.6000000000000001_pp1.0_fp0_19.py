from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# _struct.Struct.__new__( _struct.Struct, str)
# _struct.Struct.__init__( _struct.Struct, str)
# _struct.Struct.pack( _struct.Struct, int)
