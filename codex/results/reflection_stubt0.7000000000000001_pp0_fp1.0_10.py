fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
 
TypeError: __code__ must be set to a code object
</code>
I get the following error:
<code>TypeError: __code__ must be set to a code object
</code>
I also tried:
<code>def fn():
    pass

gi = (i for i in ())
fn.__code__ = gi
fn()
 
TypeError: __code__ must be set to a code object
</code>
I also tried:
<code>def fn():
    pass

gi = (i for i in ())
fn.__code__ = list(gi)
fn()
 
TypeError: __code__ must be set to a code object
</code>
Why do I get this error? And how can I fix it?


A:

When you set the <code>__code__</code> on a function, it must be set to a valid function object.
The following will give you a valid function object:
<code>fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
