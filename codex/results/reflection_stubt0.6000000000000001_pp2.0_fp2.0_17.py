fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This will raise a SystemError
fn.__code__ = (i for i in ())
fn()

# This will raise a SystemError
fn.__code__ = (i for i in ())
fn()

# This will raise a SystemError
fn.__code__ = (i for i in ())
fn()

# This will raise a SystemError
fn.__code__ = (i for i in ())
fn()

# This will raise a SystemError
fn.__code__ = (i for i in ())
fn()

# This will raise a SystemError
fn.__code__ = (i for i in ())
fn()

# This will raise a SystemError
fn.__code__ = (i for i in ())
fn()

# This will raise a SystemError
fn.__code__ = (i for i in ())
fn()

# This will raise a SystemError
fn.__code__ = (i for i in ())
fn()

# This will raise a SystemError
fn.__code__ = (i for i in ())
fn()
