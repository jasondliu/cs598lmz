fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# The following is not supported:
# fn.__code__ = gi

# The following is not supported:
# fn.__code__ = gi.gi_code.co_code

# The following is not supported:
# fn.__code__ = gi.gi_code.co_consts

fn.__code__ = gi.gi_code
fn.__code__.co_code = gi.gi_code.co_code
fn.__code__.co_consts = gi.gi_code.co_consts
fn()

# The following is not supported:
# fn.__code__.co_code = gi

# The following is not supported:
# fn.__code__.co_consts = gi

# The following is not supported:
# fn.__code__.co_code = gi.gi_code.co_code

# The following is not supported:
# fn.__code__.co_consts = gi.gi_code.co_consts
