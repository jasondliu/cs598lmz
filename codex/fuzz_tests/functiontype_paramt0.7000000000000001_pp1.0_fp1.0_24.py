from types import FunctionType
list(FunctionType(lambda p1: p1, globals())(x) for x in [1,2,3])
</code>
This gives:
<code>[&lt;function &lt;lambda&gt; at 0x7f0a26a3e950&gt;,
 &lt;function &lt;lambda&gt; at 0x7f0a26a3e9d0&gt;,
 &lt;function &lt;lambda&gt; at 0x7f0a26a3ea50&gt;]
</code>
As you can see, the lambdas are different, but the code is identical. You can check this by inspecting <code>&lt;lambda&gt;.__code__</code>.

