from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])

print(FunctionType(a.gi_code, {}).__name__)
print(FunctionType(b.gi_code, {}).__name__)
</code>
output:
<code>&lt;genexpr&gt; 
&lt;genexpr&gt; 
</code>

