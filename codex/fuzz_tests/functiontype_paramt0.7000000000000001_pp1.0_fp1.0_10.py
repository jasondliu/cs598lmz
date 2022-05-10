from types import FunctionType
list(FunctionType(lambda x: x, {'x': 1}))
</code>
This is clearly a bug, since the function has no <code>__len__</code>, but it seems that's not the case.
So, is there any way to make a list of functions in Python?


A:

Use a list of functions, not a list of functions' values.
<code>&gt;&gt;&gt; def f(x): return x
... 
&gt;&gt;&gt; def g(x): return x+1
... 
&gt;&gt;&gt; l = [f, g]
&gt;&gt;&gt; [fn(4) for fn in l]
[4, 5]
</code>

