import types
types.new_class("x")
</code>
However, <code>types</code> doesn't contain the function <code>new_class</code>, and I can't find it in any of the other documentation.
What is the function new_class, and what is the closest way to emulate it?


A:

<code>types.new_class</code> is just a helper function to create a new <code>type</code> instance - all it does is call <code>type()</code>:
<code>&gt;&gt;&gt; import types
&gt;&gt;&gt; types.new_class('A')
&lt;class '__main__.A'&gt;
&gt;&gt;&gt; type('A', (), {})
&lt;class '__main__.A'&gt;
</code>
The <code>type</code> function itself is documented:
<blockquote>
<p><code>&lt;code&gt;type(object) -&amp;gt; the object's type&lt;/code&gt;</code></
