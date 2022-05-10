from _struct import Struct
s = Struct.__new__(Struct)
s.format = '&gt;i'
bytes(s.pack(x))
</code>

<code>struct.pack</code> accepts arbitrary strings of format codes, and even arbitrary bytes. In python3's C implementation, it uses a local function <code>_PyStruct_Pack()</code> to actually reduce the argument to a number of bytes - the result of calling <code>_PyString_FormatLong()</code> with a format like <code>'%d'</code>. Then, the result of actually encoding the value with <code>sprintf()</code> is passed to <code>PyString_FromStringAndSize()</code>, and the returned value (a <code>PyBytes</code> object) is unpacked into a predefined buffer that is used for the <code>PyBytes</code> object. This essentially means that <code>struct.pack</code> can be used to construct any textually valid array of bytes, equivalent to a <code>PyBytes</code> object, although some encoding of values is still performed.

