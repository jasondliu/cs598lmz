from _struct import Struct
s = Struct.__new__(Struct)
class tst(Struct):
	_fields_ = [ ("b", c_byte), ("i", c_int)]


t = tst(20)
