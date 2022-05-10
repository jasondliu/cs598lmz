import ctypes
ctypes.cast(b, ctypes.POINTER(b.type))
</code>

Other notes (since this is the top search result):
If you need to manipulate byte order, use <code>struct</code>:
<code>b = struct.pack('&lt;dd', *data)  # new byte order
data = struct.unpack('&gt;dd', b)  # get all doubles as a tuple, default byte order
</code>
BYTEORDER
<blockquote>
<p>The byte order of the machineistored as <code>&lt;code&gt;sys.byteorder&lt;/code&gt;</code>: <code>&lt;code&gt;sys.byteorder&lt;/code&gt;</code> =
  ‘big’ on a big-endian (most significant byte first) machine, <code>&lt;code&gt;sys.byteorder&lt;/code&gt;</code>
  = ‘little’ on a little-endian (least significant byte first) machine.
  Thus, whether you can do this depends on the
