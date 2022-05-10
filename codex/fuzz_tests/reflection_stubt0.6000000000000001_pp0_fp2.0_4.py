fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: None)()
fn.__code__.co_code = b'\x00'
sys.setrecursionlimit(100000)
print(fn.__code__.co_code)
fn()
