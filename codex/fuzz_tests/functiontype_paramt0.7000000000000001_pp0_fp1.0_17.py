from types import FunctionType
list(FunctionType(a) for a in [1,2,3])
</code>
There's a problem:
<code>Traceback (most recent call last):
File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'int' object is not iterable
</code>
And if I use:
<code>list(a for a in [1,2,3])
</code>
it works, so I have to define a generator:
<code>def g(a):
    return FunctionType(a)

list(g(a) for a in [1,2,3])
</code>
But the <code>g</code> function returns <code>None</code> and the list contains <code>None</code>s.
How can I do it in a more elegant way?


A:

This is how you do it.
<code>&gt;&gt;&gt; [FunctionType(a) for a in [1,2,3]]
[&lt;function FunctionType.&lt;locals&gt;
