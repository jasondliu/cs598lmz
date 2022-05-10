fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print(fn())

# TypeError: 'generator' object is not callable
# fn.__code__ = (i for i in ())
# print(fn())
