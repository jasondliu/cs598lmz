fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ = None
fn = lambda: None
fn.__code__ = None
fn()

# __code__ = 1
fn = lambda: None
fn.__code__ = 1
fn()

# __code__ = "s"
fn = lambda: None
fn.__code__ = "s"
fn()

# __code__ = ""
fn = lambda: None
fn.__code__ = ""
fn()

# __code__ = {}
fn = lambda: None
fn.__code__ = {}
fn()

# __code__ = []
fn = lambda: None
fn.__code__ = []
fn()

# __code__ = ()
fn = lambda: None
fn.__code__ = ()
fn()

# __code__ = set()
fn = lambda: None
fn.__code__ = set()
fn()

# __code__ = frozenset()
fn = lambda: None
fn.__code__ = frozenset()
fn()

# __code__ = True
fn = lambda:
