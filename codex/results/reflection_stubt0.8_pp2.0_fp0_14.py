fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()  # Should not crash
finally:
    sys.setrecursionlimit(old_rec)  # Avoid a warning
