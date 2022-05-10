fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn() # TypeError: 'generator' object is not callable
</code>
Of course, a generator can't be called, but we're not calling it, we're calling the function, which is a different thing.
The <code>__code__</code> attribute of a function is supposed to be a code object, but the code object is only used to derive the function's <code>__name__</code> attribute and the function's <code>__defaults__</code> attribute, and to provide the default argument values if no value is provided for that argument.
So we can do this:
<code>&gt;&gt;&gt; fn.__code__ = lambda: None
&gt;&gt;&gt; fn()
&gt;&gt;&gt; fn.__code__ = lambda i: i
&gt;&gt;&gt; fn() # TypeError: &lt;lambda&gt;() missing 1 required positional argument: 'i'
&gt;&gt;&gt; fn(1)
1
&gt;&gt;&gt; fn(1, 2)
