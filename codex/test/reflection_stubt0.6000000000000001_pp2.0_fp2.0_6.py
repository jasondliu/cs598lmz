fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# function object with strange __code__ object
def strange_fn():
    pass
