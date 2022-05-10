from types import FunctionType
list(FunctionType(2+4j,4.4,'first func',("module","type")))

Output:
TypeError: cannot create 'function' instances
</code>
<blockquote>
<p>Why it is throwing error?</p>
</blockquote>
And again in multiple  parameters do not support in <code>__init__</code> of <code>FunctionType</code> it is throwing error.
Now lets create <code>class</code> type
<code>&gt;&gt;&gt; from types import FunctionType
&gt;&gt;&gt; class Custom():
...     def __init__(self, x, y):
...             self.x = x
...             self.y = y
... 
&gt;&gt;&gt; list(Custom(2+4j,4.4,''))
[2j, 4.4, '']

&gt;&gt;&gt; type(Custom(2+4j,4.4,''))
&lt;class '__main__.Custom'&gt;
</code>
Is it <code>__
