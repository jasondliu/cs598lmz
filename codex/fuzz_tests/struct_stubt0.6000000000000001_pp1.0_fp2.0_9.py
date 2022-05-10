from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)
</code>
And you will see that the <code>__new__</code> method is called with <code>Struct</code> as the first argument, and <code>'i'</code> as the second argument. The <code>__init__</code> method is called with <code>s</code> as the first argument, and <code>'i'</code> as the second argument.

