from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f') for f in (lambda: None, lambda: None))
</code>
I don't have any access to the <code>types</code> module, so I can't do that.


A:

Though it's not possible to do what you've done with just <code>map</code>, you may be able to use <code>itertools.starmap</code>:
<code>from itertools import starmap


def func1():
    global foo
    foo = 1


def func2():
    global foo
    foo = 2


funcs = [func1, func2]

starmap(lambda f: f(), (() for f in funcs))

print(foo)


&gt;&gt; 2
</code>
If you're looking to apply a list of arguments to each function instead, you could use <code>itertools.product</code> to create a list of tuples that you could star-unpack.
<code>from itertools import starmap
from itertools import product


