from types import FunctionType
list(FunctionType(add.__code__, globals()))
</code>
The output will be:
<code>[&lt;function add at 0x0000000003E726A8&gt;, &lt;function add at 0x0000000003E726E0&gt;, &lt;function add at 0x0000000003E72710&gt;]
</code>

