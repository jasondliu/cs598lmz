fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__.co_varnames

TypeError: 'generator' object is not subscriptable
</code>
If you want to get a list of variables in a generator, you'll need to inspect the generator's code object. This can be done with the <code>inspect</code> module (you can see all the function's arguments, but you'll have to filter out the ones you're not interested in):
<code>import inspect

def gen():
    a = 5
    b = 6
    c = 7
    yield a + b + c

inspect.getargspec(gen)
</code>
Outputs:
<code>ArgSpec(args=[], varargs=None, keywords=None, defaults=None)
</code>
You could then filter the <code>args</code> list for the arguments you're interested in.

