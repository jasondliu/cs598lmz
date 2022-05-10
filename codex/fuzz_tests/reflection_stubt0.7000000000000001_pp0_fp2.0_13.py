fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# create from a dict
d = dict(globals(), **locals())
fn.__code__ = d
fn()

# create from a list
l = list(globals())
fn.__code__ = l
fn()

# create from a set
s = set(globals())
fn.__code__ = s
fn()

# create from a frozenset
s = frozenset(globals())
fn.__code__ = s
fn()

# create from an array
a = array('i', range(10))
fn.__code__ = a
fn()

# create from a memoryview
m = memoryview(bytes(range(10)))
fn.__code__ = m
fn()

# create from a deque
d = deque(range(10))
fn.__code__ = d
fn()

# create from an OrderedDict
od = OrderedDict.fromkeys(range(10))
fn.__code__ = od
fn()

# create from a Counter
c
