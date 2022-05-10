from _struct import Struct
s = Struct.__new__(Struct)
filename = "Adobe.otf"


s.file = file(filename,"rb")

s.header = s.file.read(10)

s.numTables, s.searchRange, s.entrySelector, s.rangeShift = s.header

# s.file.seek(12) s.file.read(20)

s.file.seek(12)
