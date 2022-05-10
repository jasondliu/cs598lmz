fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
</code>
Then, we can do this:
<code>class Foo:
    pass

Foo.__dict__['__call__'] = lambda self: "foo"

f = Foo()
f()
#=&gt; "foo"
</code>
So, this isn't a good way to create a function, but I'm not sure why it's not a good way.

