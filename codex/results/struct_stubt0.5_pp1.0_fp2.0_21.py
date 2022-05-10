from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
</code>
Note that the <code>__init__</code> method is not called when the class is subclassed.

