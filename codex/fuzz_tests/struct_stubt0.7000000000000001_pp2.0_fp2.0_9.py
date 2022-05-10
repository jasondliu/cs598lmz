from _struct import Struct
s = Struct.__new__(Struct)
</code>
You can also use <code>type(Struct)</code> to get the type of <code>Struct</code>.  It is also a <code>type</code> object.  It is the type of the <code>Struct</code> class.  The <code>Struct</code> class is a subclass of <code>type</code>.  Using <code>type(Struct)</code> is different from <code>type(s)</code>.  <code>type(s)</code> will return a new instance of the <code>Struct</code> class.

