fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(
    0, 0, 0, 0, 0, b'', (), (), (), "", "", 0, b""
)

pickle.dumps(fn)
</code>
Results in a <code>ValueError</code>:
<blockquote>
<p>ValueError: code: arg count</p>
</blockquote>
The fix is relatively simple, just replace <code>0</code> with <code>0x0</code> in the <code>func_code</code> definition:
<code>fn.__code__ = gi.gi_code = types.CodeType(
    0x0, 0, 0, 0, 0, b'', (), (), (), "", "", 0, b""
)
</code>
(You could also use a <code>x</code> instead of the <code>0</code> in the <code>argcount</code> position of the tuple, you'll get a different error though.)
What's happening is that the <code>argcount</code> is actually an unsigned short packed into an
