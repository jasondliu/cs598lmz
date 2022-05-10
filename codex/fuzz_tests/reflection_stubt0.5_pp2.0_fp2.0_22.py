fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
</code>
<blockquote>
<pre><code>&lt;code&gt;Traceback (most recent call last):
  File "&amp;lt;stdin&amp;gt;", line 1, in &amp;lt;module&amp;gt;
  File "&amp;lt;stdin&amp;gt;", line 2, in &amp;lt;lambda&amp;gt;
TypeError: 'generator' object is not callable
&lt;/code&gt;</code></pre>
</blockquote>

