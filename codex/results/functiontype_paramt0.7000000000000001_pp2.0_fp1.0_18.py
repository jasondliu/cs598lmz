from types import FunctionType
list(FunctionType(f.__code__, {}, "test"))
#[&lt;function test.&lt;locals&gt;.&lt;listcomp&gt; at 0x1006a21e0&gt;]
</code>

