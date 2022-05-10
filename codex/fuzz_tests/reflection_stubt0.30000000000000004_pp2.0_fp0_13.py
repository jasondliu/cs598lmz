fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: __code__ must be set to a code object
</code>
I'm not sure why this is happening. I can't find anything in the docs that says that <code>fn.__code__</code> must be a code object. I can't find anything in the source that says that <code>fn.__code__</code> must be a code object. I can't find anything in the source that says that <code>fn.__code__</code> must be a code object.
So why is this happening?

