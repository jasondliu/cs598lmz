from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("&lt;")
print s.size
</code>
The documentation of _struct is here:
http://docs.python.org/2/library/struct.html#module-_struct

