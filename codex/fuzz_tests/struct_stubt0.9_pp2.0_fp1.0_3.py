from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(i='>i')
</code>
After this, you have a mutable object that accepts the required arguments and has the requested methods, exactly like when you call the actual class.

