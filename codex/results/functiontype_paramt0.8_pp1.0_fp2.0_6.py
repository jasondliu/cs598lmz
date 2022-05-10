from types import FunctionType
list(FunctionType())

# TypeError: descriptor '__iter__' of 'list' object needs an argument
</code>
Anyway, I don't think <code>list</code>'s <code>__iter__</code> implementation is correct:
<blockquote>
<pre><code>&lt;code&gt;def __iter__(self):
    return iter(self[:])
&lt;/code&gt;</code></pre>
</blockquote>
That should probably return <code>self</code> instead, although I can't think of any valid use-cases for <code>list.__iter__(FunctionType())</code> (assuming we want to keep <code>FunctionType.__iter__</code>).

