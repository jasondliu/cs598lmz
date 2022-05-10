fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
&gt;&gt;&gt; TypeError: &lt;generator object &lt;lambda&gt; at 0x7f2f8b44cac0&gt; is not a code object
</code>

