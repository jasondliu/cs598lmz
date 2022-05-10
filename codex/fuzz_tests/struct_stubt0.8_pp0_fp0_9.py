from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(str("&lt;I"))
s.size
</code>
<blockquote>
<p><code>&lt;code&gt;4&lt;/code&gt;</code></p>
</blockquote>
You can can try to get the format string from <code>struct.pack()</code> and <code>struct.unpack()</code>, but it is slightly more complicated. 
<code>import struct
s = struct.Struct(str("&lt;I"))
s.size
</code>
<blockquote>
<p><code>&lt;code&gt;4&lt;/code&gt;</code></p>
</blockquote>

