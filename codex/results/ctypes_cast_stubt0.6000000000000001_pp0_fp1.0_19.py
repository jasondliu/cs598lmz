import ctypes
ctypes.cast(p, ctypes.c_void_p).value
</code>
Here's a complete example:
<code>&gt;&gt;&gt; from ctypes import *
&gt;&gt;&gt; p = create_string_buffer(b'hello')
&gt;&gt;&gt; p.raw
b'hello'
&gt;&gt;&gt; c_void_p.from_buffer(p).value
140129889314400
</code>

