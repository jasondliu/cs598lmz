from _struct import Struct
s = Struct.__new__(Struct)

s.__init__('c')
s.unpack(b'x')
</code>
This will work, but it's not what you want.  It's just an example of how to use <code>__new__</code>.  What you want is to derive from <code>Struct</code> and override <code>__init__</code>.  Here's a simple example:
<code>from _struct import Struct

class MyStruct(Struct):
    def __init__(self, fmt_string):
        self.fmt_string = fmt_string
        super().__init__(fmt_string)
</code>
Now you can do:
<code>s = MyStruct('c')
s.unpack(b'x')
</code>

