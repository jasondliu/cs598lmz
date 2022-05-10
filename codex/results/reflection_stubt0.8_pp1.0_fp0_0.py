fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()
fn.__code__ = 1

class A:
    pass

for code in (None, 0, 0.0, '', (), [], {}, A(), A, fn, fn.__code__, gi):
    try:
        fn.__code__ = code
    except TypeError as e:
        print(e)

print(fn.__code__)
