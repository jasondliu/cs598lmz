fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()  # infinite loop
</code>
As you can see in the code, I create a function <code>fn</code> and set a generator as its <code>__code__</code> attribute.
When I call <code>fn</code>, I get an infinite loop.
I'm not sure what the loop is doing and how the <code>yield</code> statement comes into play.
Can someone explain this behavior?

