import ctypes
ctypes.cast(ctypes.pointer(int(Foo)), ctypes.c_void_p).value = 0  # note Foo, not foo
</code>
Because <code>__hash__</code> is used by the CPython interpreter to emulate <code>dict</code> keys, no dictionary-like object allows the use of mutable objects as keys.  E.g.,
<code>&gt;&gt;&gt; {Foo(): 1}
...
TypeError: unhashable type: 'Foo'
</code>
And, because the use of <code>__hash__</code> is so common, the Dunder Methods page has this to say about it:
<blockquote>
<p>There are no implied relationships among the equivalence relationship
  (represented by <code>&lt;code&gt;==&lt;/code&gt;</code>, the equivalence relationship (represented by <code>&lt;code&gt;__cmp__()&lt;/code&gt;</code>,
  and the hashability of an object (determined by <code>&lt;code&gt;__hash
