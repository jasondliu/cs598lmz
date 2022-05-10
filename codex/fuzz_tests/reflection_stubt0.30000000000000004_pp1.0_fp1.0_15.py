fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_filename

# __code__.co_filename is writable
fn = lambda: None
fn.__code__.co_filename = 'foo'
fn.__code__.co_filename

# __code__.co_filename is writable
fn = lambda: None
fn.__code__.co_filename = 'foo'
fn.__code__.co_filename

# __code__.co_filename is writable
fn = lambda: None
fn.__code__.co_filename = 'foo'
fn.__code__.co_filename

# __code__.co_filename is writable
fn = lambda: None
fn.__code__.co_filename = 'foo'
fn.__code__.co_filename

# __code__.co_filename is writable
fn = lambda: None
fn.__code__.co_filename = 'foo'
fn.__code__.co_filename

# __code__.co_filename is writable
fn = lambda: None
fn.__code
