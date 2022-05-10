fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
unpickled = pickle.loads(pickle.dumps(fn))

unpickled()
 
# Pickle a function that has a __closure__
def fn(x):
    def nested(y):
        return x + y
    return nested
fn2 = fn(2)
fn2(5)

unpickled = pickle.loads(pickle.dumps(fn2))
unpickled(5)

# Pickle a function that has a __closure__ with a cell containing a tuple
def fn(x):
    def nested(y):
        return x + y
    return nested

fn2 = fn((1, 2, 3))
fn2(5)

unpickled = pickle.loads(pickle.dumps(fn2))
unpickled(5)

# Pickle a function that has a __closure__ with a cell containing a set
def fn(x):
    def nested(y):
        return x + y
    return nested

fn2 = fn({1, 2, 3})
fn2(5)


