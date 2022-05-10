from _struct import Struct
s = Struct.__new__(Struct)
print s
s.format = 'i?f'
print s.size
s = s.__new__(s)
print s
s.format = 'i?f'
print s.size
try:
    s = Struct.__new__(Struct)
    print s
    s.format = 'i?f'
quiz()
print "-"*100
print "Now with extension classes"
from _struct import Struct
from ExtensionClass import Base
class Struct(Struct, Base):
    pass
s = Struct.__new__(Struct)
print s
s.format = 'i?f'
print s.size
s = s.__new__(s)
print s
s.format = 'i?f'
print s.size
try:
    s = Struct.__new__(Struct)
    print s
    s.format = 'i?f'
quiz()
s = Struct.__new__(Struct)
print s
s.format = 'i?f'
print s.size
print s
s = Struct.__new__(Struct, 'i
