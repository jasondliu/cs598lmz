fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__module__ = '__main__'
fn()
</code>
Output:
<code>&lt;function foo at 0x7f24d3c3e7b8&gt;
RuntimeError: generator didn't yield
</code>

