from types import FunctionType
list(FunctionType(f.__code__,globals(),'dummy',(),f.__defaults__,f.__closure__))

f.__name__
'addition'
f.__globals__
{...}
f.__closure__
</code>
Once you get the <code>__code__</code> of the function, you can call <code>dis.dis()</code> to disassemble it:
<code>&gt;&gt;&gt; from dis import dis
&gt;&gt;&gt; dis(addition)
  3           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE
</code>

