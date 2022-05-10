fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), '', '', 0, b'')
fn.__globals__ = globals()
fn()
</code>
it succesfully creates a function and calls it, but with <code>__code__ = gi.gi_code</code> it fails. I'm trying to understand the reason for the error. I suppose that the function must be initialized with an object of <code>CodeType</code> type, but <code>CodeType</code> is a class and <code>gi_code</code> is not a class instance. Why is this needed?


A:

The reason it doesn't work with <code>gi.gi_code</code> is because it is a read-only attribute. In order to set it you need to use the <code>types.FunctionType</code> constructor.
<code>&gt;&gt;&gt; fn = types.FunctionType(gi.gi_code, globals(), '')
&gt;&gt;&gt; fn()
