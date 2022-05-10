fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    pickle.dumps((fn, fn))
except pickle.PicklingError:
    print("SKIP")
    raise SystemExit


def g():
    yield 1


def f():
    yield from g()


class C:
    def __reduce__(self):
        yield g()


pickle.loads(pickle.dumps(C()))
pickle.loads(pickle.dumps(f))
