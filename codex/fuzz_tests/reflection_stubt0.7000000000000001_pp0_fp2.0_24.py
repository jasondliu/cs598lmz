fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
#fn.__code__.co_code = (i for i in ())

print(fn.__code__)
print(fn.__code__.co_code)

fn.__code__.co_code = (i for i in ())

print(fn.__code__)
print(fn.__code__.co_code)
