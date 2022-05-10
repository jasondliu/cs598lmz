fn = lambda: None
# Test fn.__code__.
fn.__code__.co_argcount
fn.__code__.co_varnames
fn.__code__.co_filename

# Test fn.__code__.co_lnotab.
fn.__code__.co_lnotab
len(fn.__code__.co_lnotab)
fn.__code__.co_lnotab.split(b'\x00')
fn.__code__.co_lnotab.split(b'\x01')
fn.__code__.co_lnotab.split(b'\x00', b'\x01')
fn.__code__.co_lnotab.split(b'\x01', b'\x00')
fn.__code__.co_lnotab.split()

## .co_consts
fn.__code__.co_consts
len(fn.__code__.co_consts)
fn.__code__.co_consts == ('',)
fn.__code__.co_consts == (None,)
fn.__
