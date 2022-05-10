from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hhl'
s.size = calcsize(s.format)
t = (1, 2, 3)
</code>
For the <code>__new__</code> call one can also give the format string as parameter:
<code>from _struct import Struct
s = Struct.__new__(Struct, 'hhl')
</code>
I would not recommend using this method as it would not be a supported behaviour but as Alex Martelli explained in his answer, it might be safe to use.

