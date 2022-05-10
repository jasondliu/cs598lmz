from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f', (True).to_bytes(1, 'little'))
s.size

s = Struct.__new__(Struct)
s.__init__('i?f')
