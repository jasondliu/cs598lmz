from _struct import Struct
s = Struct.__new__(Struct)
file = open('keyfile')
keyfile = file.read()
file.close()
