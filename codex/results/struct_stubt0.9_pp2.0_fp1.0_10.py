from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__['format'] = 'I 5s f'
s.__dict__['size'] = calcsize(s.format)
</code>
to
<code>from _struct import Struct
s = Struct('I 5s f')
</code>
or if you want <code>s.size</code> you either need to set it, or just call <code>calcsize</code> again when you need it rather than caching it.
You don't really need to know what Struct does behind the scenes, it's enough to know that it's effectively an opaque struct object that you fiddle with, there's no reason you should set <code>__dict__</code> entries directly like that.

