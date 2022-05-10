from _struct import Struct
s = Struct.__new__(Struct)
</code>
Depending on what you actually want to do, <code>Struct.__new__</code> may consume the arguments you supply it, similar to what happens when you instantiate a <code>Struct</code> instance normally.
<blockquote>
<p>How can I use a Struct to manipulate binary data if I don't have the format string when I create a Struct object?</p>
</blockquote>
You can't create a <code>Struct</code> without a format string, but you can create an instance of the class, and later alter its format string:
<code>import _struct
s = _struct.Struct()
s.format = "h"
</code>
You can only use the last format string supplied to the <code>Struct.format</code> attribute to pack and unpack data, though. If you're trying to pack and unpack data using multiple formats specified at runtime, you'll have to use the <code>_struct</code> module directly.

