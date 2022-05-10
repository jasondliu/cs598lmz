fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print(fn()) # None

# We can assign value to a fn
fn.__code__ = 42
print(fn()) # 42

# fn.__call__ also returns a function
fn.__call__.__code__ = lambda: 'a function'

# We can call fn like fn()
print(fn()) # a function
