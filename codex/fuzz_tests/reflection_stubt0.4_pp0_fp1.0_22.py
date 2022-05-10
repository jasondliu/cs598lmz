fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'generator' object is not callable

# ------------------------------------------------------------

fn = lambda: None
fn.__code__ = 1
fn()

# TypeError: 'int' object is not callable

# ------------------------------------------------------------

fn = lambda: None
fn.__code__ = 'abc'
fn()

# TypeError: 'str' object is not callable

# ------------------------------------------------------------

fn = lambda: None
fn.__code__ = fn
fn()

# TypeError: 'function' object is not callable

# ------------------------------------------------------------

fn = lambda: None
fn.__code__ = None
fn()

# TypeError: 'NoneType' object is not callable

# ------------------------------------------------------------

fn = lambda: None
fn.__code__ = True
fn()

# TypeError: 'bool' object is not callable

# ------------------------------------------------------------

fn = lambda: None
fn.__code__ = False
fn()

# TypeError: 'bool' object is not callable

# --------------------------------
