fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
new = type(meth)(meth.__func__.__code__, globals(), meth.__name__,
                 meth.__defaults__, meth.__closure__)
new.__dict__.update(meth.__dict__)
new.__self__ = f
return new
</code>
It's a bit long, but all it does is create a copy of the decorated method, with the custom <code>self</code> instance.

