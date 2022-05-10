from _struct import Struct
s = Struct.__new__(Struct)
s.__init__()
s.__init__('l')
s.__init__('l', 'buffer')
s.__init__('=l')
s.__init__('=l', 'buffer')

# test __reduce__
import sys
s = Struct.__new__(Struct)
s.__init__('l')
s.__reduce__()
s.__reduce__(42)
s = Struct.__new__(Struct)
s.__init__('l', 'buffer')
s.__reduce__()
s.__reduce__(42)

# test __reduce_ex__
import sys
s = Struct.__new__(Struct)
s.__init__('l')
s.__reduce_ex__(2)
s.__reduce_ex__(2, 42)
s = Struct.__new__(Struct)
s.__init__('l', 'buffer')
s.__reduce_ex__(2)
s.__reduce_ex__(2, 42)

