from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
</code>
Note the <code>i?f</code> which is specific to the Python <code>struct</code> module. You can get the required format string by using the <code>unpack()</code> function:
<code>fmtstring = s.unpack.func_defaults[0]
</code>
In the case of my example <code>s.unpack.func_defaults</code> is a tuple with one item, a string representing the struct format <code>"i?f"</code>.

