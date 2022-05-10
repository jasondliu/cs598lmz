fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

callable(fn)

fn()

# try:
#     fn()
# except TypeError as e:
#     print(e)
