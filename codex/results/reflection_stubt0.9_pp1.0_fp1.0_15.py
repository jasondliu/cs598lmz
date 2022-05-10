fn = lambda: None
gi = (i for i in ())
fn.__code__ = weakref.proxy(gi)
fn.__qualname__ = ''
compile('def fn(): pass\n', '', 'exec')
fn.__code__ = weakref.proxy(gi)
