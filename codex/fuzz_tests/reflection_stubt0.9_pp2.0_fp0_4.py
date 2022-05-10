fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
func(*fn.__code__.co_varnames)
</code>
Although this isn't intended to be secure (I don't know if there's a security bug in <code>iter</code> for example), it's also probably more than fast enough for your purposes. I wouldn't use it for anything security related though, because code objects aren't meant to be created from bare iterators.

