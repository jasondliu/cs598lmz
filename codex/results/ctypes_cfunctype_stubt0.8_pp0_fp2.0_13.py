import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
</code>
This works, but I get a warning that the "return value was ignored", and the line the warning points at is the definition of <code>FUNTYPE</code>, so I don't know how to suppress it.
How can I suppress just this warning?  Or is there a better way to prevent this warning when using <code>ctypes</code>?


A:

<blockquote>
<p>How can I suppress just this warning?</p>
</blockquote>
it should be as simple as:
<code>import warnings
warnings.filterwarnings("ignore", ".*return value was ignored.*")
</code>

