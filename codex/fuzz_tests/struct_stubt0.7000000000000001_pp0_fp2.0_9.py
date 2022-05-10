from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('QQQQ')
</code>
If you want to use the same class name, you have to inherit from <code>Struct</code> and override <code>__new__</code> (so that it doesn't call <code>super().__new__</code>).
<code>from _struct import Struct
class NewStruct(Struct):
    def __new__(cls, fmt):
        self = cls.__dict__['__new__'](cls)
        self.__init__(fmt)
        return self
</code>

