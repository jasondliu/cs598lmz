from _struct import Struct
s = Struct.__new__(Struct)
_struct.Struct.__init__(s, '>l')
data = s.pack(_int)
</code>
But is there perhaps a way to do it with a single statement? A method like the following does not work:
<code>data = Struct.__new__(Struct, '&gt;l').pack(_int)
</code>
Nor does the following:
<code>data = getattr(Struct, _struct.Struct.__new__)(Struct, '&gt;l').pack(_int)
</code>
Is there some other way to do this that I am not aware of?


A:

Instead of calling <code>Struct.__new__(Struct, '&gt;l')</code> you can just create an instance:
<code>data = Struct('&gt;l').pack(_int)
</code>

