fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

fn()

# This is not supported by PyPy.

# import sys
# try:
#     sys.settrace(lambda *args: None)
# except TypeError:
#     print("SKIP")
#     raise SystemExit

# def f(): pass
# f.__code__ = f.__code__

# f()
