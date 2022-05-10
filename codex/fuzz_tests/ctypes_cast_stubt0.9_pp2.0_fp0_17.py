import ctypes
ctypes.cast(1, ctypes.py_object)
</code>
You get:
<blockquote>
<pre><code>&lt;code&gt;Traceback (most recent call last):
  File "&amp;lt;stdin&amp;gt;", line 1, in &amp;lt;module&amp;gt;
TypeError: an integer is required (got type int)
&lt;/code&gt;</code></pre>
</blockquote>
But, if you run the same code:
<code>import ctypes
ctypes.cast(ctypes.c_int(1), ctypes.py_object)
</code>
You get:
<blockquote>
<pre><code>&lt;code&gt;&amp;lt;cparam 'P' (0x7fe27051b140)&amp;gt;
&lt;/code&gt;</code></pre>
</blockquote>
Which is the ctypes "representation" of a <code>py_object</code>
Not much to go on, but it's more than you have right now
