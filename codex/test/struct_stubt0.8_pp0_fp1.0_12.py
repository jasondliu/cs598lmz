from _struct import Struct
s = Struct.__new__(Struct)
#s = Struct("!f", float("nan")).unpack(open("test.dat", 'rb').read())[0]
s.format = "!f"
s.size = 4
