import ctypes
ctypes.cast(foo, ctypes.c_void_p).value
</code>
However, <code>ctypes.cast</code> is officially documented as:
<blockquote>
<p><code>&lt;code&gt;ctypes.cast(obj, typ)&lt;/code&gt;</code></p>
<p>Creates a new instance of the type <em>typ</em> by casting the <em>obj</em> argument.
  Casting objects is supported in a similar fashion than in C. It may be
  used to cast only to pointers and to c_char_p.</p>
</blockquote>
That description seems to imply that you're supposed to use <code>ctypes.cast</code> only for casting to pointer types, and furthermore only to a specific subset of pointer types.  I haven't tested it, but can't guarantee that casting to <code>c_void_p</code> will work in any Python version (and <code>cast</code> arguably doesn't even make sense if you only have the value and not the pointer, so I'm pretty confident it's not something you should be doing
