fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'generator' object is not callable
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "&lt;stdin&gt;", line 1, in &lt;module&gt;
# TypeError: 'generator' object is not callable
</code>

