from _struct import Struct
s = Struct.__new__(Struct)
</code>
Note: There is actually no need to create a <code>Struct</code> from scratch. Just use <code>struct.Struct('I')</code>.

