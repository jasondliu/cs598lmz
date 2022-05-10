fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: &lt;lambda&gt;() takes 0 positional arguments but 1 was given
</code>

