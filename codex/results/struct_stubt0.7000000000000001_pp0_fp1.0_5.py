from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
print s.pack("x")
</code>
See http://docs.python.org/2/library/struct.html#format-characters for the format characters.
And http://docs.python.org/2/library/struct.html#struct-alignment for the alignment, size and packing.

