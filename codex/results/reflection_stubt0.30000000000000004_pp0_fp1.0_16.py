fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# The following will fail with a TypeError:
# fn()

# This is the expected behaviour, as the code object is not callable.
# However, the repr of the code object is not very useful:
print(fn.__code__)

# It would be nice if the repr of the code object would include the name of
# the function it is attached to.
# This is the case in Python 3.5.
# In Python 3.6, the repr of the code object is even more informative:
# &lt;code object fn at 0x7f9b9e9d8a40, file "&lt;stdin&gt;", line 1&gt;
</code>

