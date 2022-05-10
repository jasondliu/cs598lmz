fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "fn"
fn.__qualname__ = "fn"
fn.__module__ = "__main__"

print(fn.__code__)
print(fn.__qualname__)
print(fn.__module__)
