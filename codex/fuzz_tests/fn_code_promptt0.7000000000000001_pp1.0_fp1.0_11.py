fn = lambda: None
# Test fn.__code__
fn.__code__
fn.__code__.co_argcount
fn.__code__.co_consts
fn.__code__.co_code

# Test code.__eq__
code = fn.__code__
code.__eq__(code)
code.__eq__(fn.__code__)
code.__eq__(object())

# Test code.__ne__
code.__ne__(code)
code.__ne__(fn.__code__)
code.__ne__(object())

# Test code.__repr__
code.__repr__()

# Test code.__hash__
code.__hash__()
hash(code)

# Test code.co_code
code.co_code
bytes(code.co_code)

# Test code.co_consts
code.co_consts
tuple(code.co_consts)

# Test code.co_filename
code.co_filename

# Test code.co_firstlineno
code.co_firstlineno

# Test
