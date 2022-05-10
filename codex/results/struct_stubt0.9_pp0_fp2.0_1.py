from _struct import Struct
s = Struct.__new__(Struct)
class tst(Struct):
	_fields_ = [ ("b", c_byte), ("i", c_int)]


t = tst(20)
print t.b, t.i
class tst(Struct):
	_fields_ = [ ("b", c_byte), ("i", c_int)]
	_pack_ = 1
t = tst(20)
print t.b, t.i
class tst(Structure):
	_fields_ = [ ("b", c_byte), ("i", c_int)]
	_pack_ = 1

import os
os.system('./tst')
