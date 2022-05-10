from _struct import Struct
s = Struct.__new__(Struct)
print(s.pack('hhhh', 1, 2, 3, 4))
</code>

If you you want to do the same thing with the <code>pack</code> function, you could do something like this:
<code>from _struct import Struct, unpack, pack
class Struct(Struct):
    def pack(self, *args):
        return len(args) * pack(self.format, *args)
s = Struct.__new__(Struct)
s.format = 'hhhh'
print(s.pack(1, 2, 3, 4))
</code>

