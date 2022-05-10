from types import FunctionType
list(FunctionType(f.__code__, globals(), 'myfunc').__closure__)
</code>
But it doesn't work with lambdas. <code>__closure__</code> is <code>None</code>.
<code>g = lambda x: x + y
g.__closure__
</code>
<blockquote>
<p>AttributeError: 'function' object has no attribute '__closure__'</p>
</blockquote>
How can I access the value of <code>y</code> in a lambda?


A:

Lambdas do not have closures.
<code>&gt;&gt;&gt; lambda x: x + y
&lt;function &lt;lambda&gt; at 0x00000000032D5D90&gt;
&gt;&gt;&gt; _.__closure__
&gt;&gt;&gt; 
</code>
They are created at compile time, and do not have a closure.
<code>&gt;&gt;&gt; import dis
&gt;&gt;&gt; dis.dis(
