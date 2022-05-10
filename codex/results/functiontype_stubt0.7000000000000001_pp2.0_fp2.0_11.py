from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
def f(x):
    print x
    return x
op = lambda x,y: f(x) + 1
op(a, b)

# Output:
# 1
# &lt;generator object &lt;genexpr&gt; at 0x7f2bb7e9e1a0&gt;
</code>
If you want to add two generators you can not do it, but you can use the <code>itertools</code> module to iterate over multiple generators. 
<code>from itertools import chain

a = (x for x in [1])
b = (x for x in [2])

for i in chain(a, b):
    print i

# Output:
# 1
# 2
</code>

