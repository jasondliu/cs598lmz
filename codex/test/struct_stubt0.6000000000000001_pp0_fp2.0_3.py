from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('4s')
s.pack('aaaa')
s.pack('bbbb')
s.pack('cccc')
s.pack('dddd')
s.pack('eeee')
