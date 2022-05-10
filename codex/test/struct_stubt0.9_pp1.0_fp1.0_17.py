from _struct import Struct
s = Struct.__new__(Struct)
#s._map = 'hi'
s.__init__('hi')
data = 'abc' #(12, 45)
s.pack(data)
