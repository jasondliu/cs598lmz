from types import FunctionType
list(FunctionType(f.func_code,f.func_globals))
</code>
returns:
<code>[&lt;function f at 0x7f479fb7ff28&gt;]
</code>

