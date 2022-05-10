from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i")
s.unpack("\x00\x00\x00\x00")
</code>
The above code works, but I don't know why?
I have read the source code of <code>_struct</code> module, but I still don't understand why it works.

