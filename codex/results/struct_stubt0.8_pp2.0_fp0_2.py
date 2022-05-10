from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda : 5
print s.size()
</code>

