from types import FunctionType
list(FunctionType(lambda x: 2*x))
</code>
However, this would yield a list of the same function, rather than a list of the function's return value at different input values.
<code>&gt;&gt;&gt; list(FunctionType(lambda x: 2*x))
[&lt;function &lt;lambda&gt; at 0x10b5c5b70&gt;, &lt;function &lt;lambda&gt; at 0x10b5c5b70&gt;, &lt;function &lt;lambda&gt; at 0x10b5c5b70&gt;, &lt;function &lt;lambda&gt; at 0x10b5c5b70&gt;, &lt;function &lt;lambda&gt; at 0x10b5c5b70&gt;, &lt;function &lt;lambda&gt; at 0x10b5c5b70&gt;, &lt;function &lt;lambda&gt; at 0x10b5c5b70&gt;, &lt;function &lt;lambda&gt; at 0x
