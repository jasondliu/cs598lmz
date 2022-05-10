fn = lambda: None
# Test fn.__code__.co_flags bitfield.
fn.__code__.co_flags = fn.__code__.co_flags | CO_VARARGS
