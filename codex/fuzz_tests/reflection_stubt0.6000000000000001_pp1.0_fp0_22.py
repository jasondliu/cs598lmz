fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "foo"
fn.__module__ = ""
print(fn.__code__)
print(fn.__name__)
print(fn.__module__)
print(fn.__closure__)
</code>
<code>&lt;code object &lt;genexpr&gt; at 0x00BC8C80, file "&lt;stdin&gt;", line 1&gt;
foo

None
</code>

