fn = lambda: None
# Test fn.__code__.co_filename exists and is not None
fn.__code__ = dir()
print("Called Example foo.py with __code__ Method !")
print()
