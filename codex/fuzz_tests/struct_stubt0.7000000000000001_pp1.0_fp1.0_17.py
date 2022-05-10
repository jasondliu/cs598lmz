from _struct import Struct
s = Struct.__new__(Struct)
for i in xrange(5): s.pack(i)
</code>
This is a good way to make a new class that inherits from <code>Struct</code>, but I'm not sure how to do it with a <code>Struct</code> object. I want <code>s</code> to be a <code>Struct</code> that has 5 pre-defined packs.

