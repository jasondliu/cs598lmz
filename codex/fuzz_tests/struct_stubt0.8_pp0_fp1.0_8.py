from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.num = 1
</code>
That will most likely create a new class derived from <code>Struct</code> and execute the body of <code>Struct.__new__</code> in the context of that new class. You can verify that by inspecting the <code>__mro__</code> of the class. So maybe <code>super</code> is a better idea:
<code>super(Struct, s).__new__(Struct, 'i')
</code>
I haven't tried it, but it's a sound approach. If that doesn't work, you can always make your own <code>__new__</code> method:
<code>class NewStruct(Struct):
    def __new__(cls, format):
        cls.format = format
        cls.num = 1
        return super(NewStruct, cls).__new__(cls, format)
</code>

