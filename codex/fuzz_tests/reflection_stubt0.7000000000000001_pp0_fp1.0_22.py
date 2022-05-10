fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'generator' object is not callable
</code>

