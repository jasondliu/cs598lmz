from _struct import Struct
s = Struct.__new__(Struct)
s.size = 4
s.format = 'hhl'
</code>
However, on Python 3.x, it seems that it will try to create a <code>Struct</code> object by calling its constructor, which just ensures that the arguments are valid.
Is there any way to access the struct module using the C API on Python 3.x?

