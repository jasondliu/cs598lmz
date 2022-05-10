from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(b'<5if')
</code>
which won't work if your <code>Struct</code> class has a <code>__new__</code> method.

2. Constructing the <code>Struct</code> instance
<code>class StructMetaclass(type):

    def __call__(cls, *args):
        # Unlike __new__, __call__ _can_ handle the right-hand-side of
        # __init__, so there's no need to create a new instance and then
        # manually call __init__.
        s = cls.__new__(cls, *args)
        s.__init__(*args)
        return s

class Struct(object, metaclass=StructMetaclass):

    def __new__(cls, fmt, byteorder=''):
        # This takes care of the left-hand-side of __init__.
        # It creates a `Struct` instance with a hardcoded format
        # string, no matter what you pass to the constructor.
        return super().__new__(
