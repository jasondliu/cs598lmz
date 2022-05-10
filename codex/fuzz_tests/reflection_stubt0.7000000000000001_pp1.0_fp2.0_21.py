fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

m = memoryview(b"123")
m.tolist() # should not crash

print("done")
