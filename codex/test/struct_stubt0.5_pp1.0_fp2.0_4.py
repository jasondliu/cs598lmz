from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', '123') # init s
print(s.size) # 4
