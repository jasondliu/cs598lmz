fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# error: a generator cannot be used to create a code object

def fn():
    gi = (i for i in ())
    fn.__code__ = gi.gi_code

# error: a generator cannot be used to create a code object

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# error: a generator cannot be used to create a code object

def fn():
    gi = (i for i in ())
    fn.__code__ = gi.gi_code

# error: a generator cannot be used to create a code object

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# error: a generator cannot be used to create a code object

def fn():
    gi = (i for i in ())
    fn.__code__ = gi.gi_code

# error: a generator cannot be used to create a code object


