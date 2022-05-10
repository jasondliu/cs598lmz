from _struct import Struct
s = Struct.__new__(Struct)
s.put('i', 123)
s.put('i', 456)
s.put('d', 3.123)
s.get('i')

s.get('i')

s.get('d')
