fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
</code>
<code>fn</code> has a <code>__code__</code> attribute, but you can't get the <code>co_argcount</code> from it:
<code>&gt;&gt;&gt; fn.__code__.co_argcount
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'generator' object has no attribute 'co_argcount'
</code>

