fn = lambda: None
# Test fn.__code__
>>> fn.__code__
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: no code object

# Test fn.__code__.co_varnames
fn.__code__.co_varnames
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'co_varnames'
</code>
But the idea of using <code>locals</code> is very much in line with what I'm looking for! Thanks.

