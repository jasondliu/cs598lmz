from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(str(endianness) + str(numtype) + str(numpoints))
