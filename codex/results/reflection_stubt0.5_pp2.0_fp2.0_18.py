fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# The following will raise TypeError:
# fn()
#
# But the following will succeed:
fn.__call__()

# And the following will succeed:
fn()
</code>
In the above example, <code>fn.__call__()</code> and <code>fn()</code> are equivalent.  So, what's the difference between <code>fn.__call__()</code> and <code>fn()</code>?


A:

The <code>__call__</code> method is a descriptor, which means that it is called when the object is accessed as an attribute. The result of the call is then used as the value of the attribute.
The <code>__call__</code> method is used to implement the call syntax for an object.

