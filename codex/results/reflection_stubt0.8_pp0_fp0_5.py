fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

print(fn)
# &lt;function &lt;lambda&gt; at 0x0000000002B7B268&gt;
print(fn())
# Traceback (most recent call last):
#   File "test.py", line 7, in &lt;module&gt;
#     print(fn())
#   File "&lt;lambda&gt;", line 1, in &lt;lambda&gt;
#   File "&lt;string&gt;", line 1, in &lt;genexpr&gt;
# StopIteration
</code>
Does <code>fn</code> behave as a generator here?


A:

<blockquote>
<p>Does <code>&lt;code&gt;fn&lt;/code&gt;</code> behave as a generator here?</p>
</blockquote>
No, <code>fn</code> is an object of type <code>function</code> that calls the generator returned by a <code>genexpr</code> when invoked. This isn't a generator expression, it's a generator.

