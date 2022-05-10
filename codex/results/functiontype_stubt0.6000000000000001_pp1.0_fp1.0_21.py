from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))

b = (x for x in [2])
print(type(b))
print(isinstance(b, FunctionType))
</code>
output:
<code>&lt;class 'generator'&gt;
True
&lt;class 'generator'&gt;
False
</code>

