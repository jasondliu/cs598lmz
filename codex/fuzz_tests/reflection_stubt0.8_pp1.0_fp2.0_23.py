fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
</code>
Now,
<code>fn()
</code>
raises
<code>TypeError: unsupported operand type(s) for -=: 'int' and 'int'
</code>
What happened? What is <code>-=</code> doing in there?

