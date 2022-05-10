fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not writable, but we can still do it.

fn = lambda: None
fn.__code__ = 1
fn()

# __code__ is not writable, but we can still do it.

fn = lambda: None
fn.__code__ = "string"
fn()

# __code__ is not writable, but we can still do it.

fn = lambda: None
fn.__code__ = None
fn()

# __code__ is not writable, but we can still do it.

fn = lambda: None
fn.__code__ = True
fn()

# __code__ is not writable, but we can still do it.

fn = lambda: None
fn.__code__ = False
fn()

# __code__ is not writable, but we can still do it.

fn = lambda: None
fn.__code__ = object()
fn()

# __code__ is not writable, but we can still do it.

fn = lambda: None
fn.__code__
