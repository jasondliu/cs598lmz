from _struct import Struct
s = Struct.__new__(Struct)
</code>
Alternatively, you can subclass <code>Struct</code> (with the same name, because the base <code>Struct</code> class doesn't use that as the name reflects the format):
<code>&gt;&gt;&gt; import _struct
&gt;&gt;&gt; class Struct(_struct.Struct):
...     pass
... 
&gt;&gt;&gt; s = Struct('!H')
&gt;&gt;&gt; s
&lt;class '__main__.Struct'&gt;
</code>
Alternatively, you can override <code>_fmt</code>:
<code>class Struct(_struct.Struct):
    def __init__(self, _fmt):
        _struct.Struct.__init__(self, '')
        self._fmt = _fmt
</code>
Note that I added an <code>'!'</code> in the <code>_struct</code> format. The <code>null_padding</code> arg you have doesn't do anything, but it looks like you may have tried to use the
