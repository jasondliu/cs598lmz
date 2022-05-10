from types import FunctionType
list(FunctionType(code, globals()) for code in codes)

# result
[&lt;function x at 0x10581c6e0&gt;, &lt;function x at 0x10581c730&gt;]
</code>

