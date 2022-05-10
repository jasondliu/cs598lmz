fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
</code>
This works in Python 2, but Python 3 is more restrictive.
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: readonly attribute
</code>
I can't find that this is explicitly disallowed, in either the documentation or the reference. It's not mentioned in the What's new in Python 3 guide either. Is there a reason for this?

I'm not actually trying to do this, but I'm just wondering if there is a documented reason for this.

