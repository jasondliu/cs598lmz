fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__module__ = 'mod'
</code>
In Python 3.6, the resulting <code>fn</code> is callable, but the stack trace is not the same as that of a normal function:
<code>&gt;&gt;&gt; fn()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 5, in fn
  File "&lt;stdin&gt;", line 5, in &lt;genexpr&gt;
StopIteration

&gt;&gt;&gt; def fn():
...     return None
... 
&gt;&gt;&gt; fn()
&gt;&gt;&gt; 
</code>
I haven't been able to find anything in the docs that explains why the resulting <code>fn</code> is not the same as the one created with <
