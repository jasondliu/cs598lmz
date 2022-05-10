fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__module__ = 'lambda()'

# Release the GIL to expose the crash
time.sleep(0.1)
