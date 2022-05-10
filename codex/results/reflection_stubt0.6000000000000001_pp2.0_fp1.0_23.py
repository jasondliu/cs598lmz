fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
# del gi

# pickle it
p = pickle.dumps(fn)

# unpickle it
fn2 = pickle.loads(p)

fn2()
