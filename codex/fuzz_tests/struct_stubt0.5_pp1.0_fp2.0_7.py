from _struct import Struct
s = Struct.__new__(Struct)
s.__init__()
s.build('&lt;B')
</code>
The last line raises the error. The problem is that <code>Struct</code> is a class, so the <code>__init__</code> method is called when the instance is created. The <code>__init__</code> method for the <code>Struct</code> class does not take any arguments. Therefore, the <code>build</code> method is never called.

