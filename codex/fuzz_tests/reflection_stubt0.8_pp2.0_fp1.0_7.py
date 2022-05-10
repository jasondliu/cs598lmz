fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
</code>
Is there any reason why this should not work? I can't imagine why it should not, since <code>__code__</code> "is a read-only attribute", so why would it check for the type?
I'm asking because <code>function.func_code</code> does that check as well, and I'd like to use a <code>function</code> object as a context manager, where I'm setting the <code>__code__</code> attribute.

