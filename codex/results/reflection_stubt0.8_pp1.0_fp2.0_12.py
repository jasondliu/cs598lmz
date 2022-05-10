fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
</code>
I get:
<code>Traceback (most recent call last):
  File "&lt;pyshell#13&gt;", line 1, in &lt;module&gt;
    fn.__code__ = gi.gi_frame.f_code
AttributeError: 'code' object has no attribute '__init__'
</code>
Why does the <code>code</code> object not have a <code>__init__</code>? Is there any way to change it?


A:

<code>code</code> objects are immutable.  You cannot change their values.  They are created by the Python compiler and contain code for a function which is then turned into a <code>function</code> object.

