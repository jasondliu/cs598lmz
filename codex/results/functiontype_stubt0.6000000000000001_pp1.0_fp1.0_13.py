from types import FunctionType
a = (x for x in [1])
b = list.__iter__([1])
print(type(a), type(b))
print(isinstance(a, FunctionType), isinstance(b, FunctionType))
</code>
prints
<code>&lt;class 'generator'&gt; &lt;class 'list_iterator'&gt;
False False
</code>

