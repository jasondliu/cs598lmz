fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# bpo-34168: segfault when using a generator expression as a code object
gi = (i for i in ())
fn = lambda: None
fn.__code__ = gi
fn()

# bpo-34168: segfault when using a dictionary comprehension as a code object
dc = {i: i for i in ()}
fn = lambda: None
fn.__code__ = dc
fn()

# bpo-34168: segfault when using a set comprehension as a code object
sc = {i for i in ()}
fn = lambda: None
fn.__code__ = sc
fn()

# bpo-34168: segfault when using a set comprehension as a code object
sc = {i for i in ()}
fn = lambda: None
fn.__code__ = sc
fn()

# bpo-34168: segfault when using a set comprehension as a code object
sc = {i for i in ()}
fn = lambda: None
fn.__code__ = sc
fn()

#
