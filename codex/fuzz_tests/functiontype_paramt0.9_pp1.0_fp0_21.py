from types import FunctionType
list(FunctionType(x.__code__, globals(), 'test') for x in (test_1,test_2,test_3))
</code>
Output:
<code>[&lt;function test_1 at 0x7f03e0a4a4d0&gt;, &lt;function test_2 at 0x7f03e09fbd70&gt;, &lt;function test_3 at 0x7f03e09fb1e0&gt;]
</code>

