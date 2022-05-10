from _struct import Struct
s = Struct.__new__(Struct) # 注意这里
s.__init__('>i') # 传入endianess和int的format spec
s.size # 返回4

