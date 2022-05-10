from types import FunctionType
list(FunctionType(f.function_code)
     for f in set(chain.from_iterable(inspect.getclosurevars(f).freevars
                                      for f in set(inspect.getmembers(mdl, inspect.isfunction)))))
</code>
Output:
<code>[&lt;function A.&lt;locals&gt;.f at 0x7fbbd3a3ad08&gt;, &lt;function B.&lt;locals&gt;.g at 0x7fbbd3a3aae8&gt;, &lt;function B.&lt;locals&gt;.h at 0x7fbbd3a4f7b8&gt;]
</code>

