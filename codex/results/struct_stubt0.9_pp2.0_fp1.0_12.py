from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
f = open(path)
ch = f.read(4)
un = s.unpack(ch)
print un
</code>
Though there are much easier solutions to this problem.

