fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# this is not an error!
fn = lambda: None
fn.__code__ = None
fn()

# this is not an error!
fn = lambda: None
fn.__code__ = False
fn()

# this is not an error!
fn = lambda: None
fn.__code__ = True
fn()

# this is not an error!
fn = lambda: None
fn.__code__ = 0
fn()

# this is not an error!
fn = lambda: None
fn.__code__ = 1
fn()

# this is not an error!
fn = lambda: None
fn.__code__ = ""
fn()

# this is not an error!
fn = lambda: None
fn.__code__ = b""
fn()

# this is not an error!
fn = lambda: None
fn.__code__ = ()
fn()

# this is not an error!
fn = lambda: None
fn.__code__ = []
fn()

# this is not an error!
fn = lambda: None
