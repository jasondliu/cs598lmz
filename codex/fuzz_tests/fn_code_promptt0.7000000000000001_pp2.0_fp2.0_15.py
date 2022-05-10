fn = lambda: None
# Test fn.__code__.co_code
fn()
# Test fn.__code__.co_consts
fn()
# Test fn.__code__.co_names
fn()
# Test fn.__code__.co_varnames
fn()
# Test fn.__code__.co_filename
fn()
# Test fn.__code__.co_name
fn()
# Test fn.__code__.co_firstlineno
fn()
# Test fn.__code__.co_lnotab
fn()
# Test fn.__code__.co_freevars
fn()
# Test fn.__code__.co_cellvars
fn()

# Test for bug #1275831
s = "def f(): pass\ndef g(): pass\n"
compile(s, "<string>", "exec")

# Test for bug #1405287
compile("print 1, #", "", "exec")

# Test for bug #1446059
compile("__import__('sys').exit(47)", "", "exec")

# Test for bug #1477
