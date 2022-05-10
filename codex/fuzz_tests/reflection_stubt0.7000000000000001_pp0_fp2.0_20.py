fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

TypeError: code expected instead of generator
</code>
And second question is, if i want to get the code from a function, this worked:
<code>def test_fn():
    return

print(test_fn.__code__)
</code>
return this:
<code>&lt;code object test_fn at 0x7f1d7091c9f0, file "&lt;stdin&gt;", line 1&gt;
</code>
But, if i will call in this way:
<code>print(test_fn().__code__)
</code>
i get this error:
<code>AttributeError: 'NoneType' object has no attribute '__code__'
</code>
Why? And how to get the code from a function if it is return something?


A:

<code>fn.__code__ = gi.gi_code</code> does not work because the <code>code</code> attribute of a function only accepts a <code>code</code> object, and not a <code>generator
