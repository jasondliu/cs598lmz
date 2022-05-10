fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Verify that the explicit __code__ attribute is used.
print(fn.__code__)

# Verify that the function still works.
print(fn())

# Verify that the __code__ attribute is writable.
fn.__code__ = lambda: None
print(fn())

# Verify that the __code__ attribute is writable even if it was previously a
# generator.
fn.__code__ = gi
print(fn())

# Verify that the __code__ attribute is writable even if it was previously a
# generator.
fn.__code__ = gi
print(fn())

# Verify that the __code__ attribute is writable even if it was previously a
# generator.
fn.__code__ = gi
print(fn())

# Verify that the __code__ attribute is writable even if it was previously a
# generator.
fn.__code__ = gi
print(fn())

# Verify that the __code__ attribute is writable even if it was previously a
# generator.
fn.__code__ = gi
print(fn())

