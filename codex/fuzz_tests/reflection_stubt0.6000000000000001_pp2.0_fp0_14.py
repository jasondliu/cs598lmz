fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# It works.

def fn():
    return 5
fn.__code__ = 5
fn()

# It works.

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__ = 5
fn()

# It works.

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__ = gi
fn()

# It works.

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__ = gi
fn.__code__ = 5
fn()

# It works.

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__ = gi
fn.__code__ = gi
fn()

# It works.

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code
