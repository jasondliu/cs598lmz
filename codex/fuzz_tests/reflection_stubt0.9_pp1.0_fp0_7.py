fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
s = fn.__code__
s.co_flags = s.co_flags) | (1 | 2)
</code>
This is to shorten the code in the question. The rest of the code is still the same.

