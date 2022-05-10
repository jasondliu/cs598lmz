fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# In this case, the function is called, but the generator is closed
# immediately.

# The following test is similar, but it uses an arbitrary function instead
# of a generator.
def fn():
    print("fn")
fn.__code__ = gi.gi_code
fn()

# The following test is similar, but it uses a generator expression instead
# of a generator.
fn.__code__ = (i for i in ()).gi_code
fn()

# The following test is similar, but it uses a list comprehension instead
# of a generator.
fn.__code__ = [i for i in ()].gi_code
fn()

# The following test is similar, but it uses a set comprehension instead
# of a generator.
fn.__code__ = {i for i in ()}.gi_code
fn()

# The following test is similar, but it uses a dict comprehension instead
# of a generator.
fn.__code__ = {i: i for i in ()}.gi_code
fn()

# The following test is
