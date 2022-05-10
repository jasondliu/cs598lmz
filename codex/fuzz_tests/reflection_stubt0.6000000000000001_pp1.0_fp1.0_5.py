fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__module__ = 'foo'
print(fn)
</code>
On Python 3.4 and Python 3.5 this prints:
<code>&lt;function fn at 0x7f7d17bcdc80&gt;
</code>
On Python 2.7 it prints:
<code>fn()
</code>

