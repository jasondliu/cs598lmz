fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "fn"
fn.__annotations__ = {"return": 1}

# This should not raise
fn()

# This should not raise
fn.__code__ = gi.gi_code

# This should not raise
fn()
