fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: __code__ assigned to non-code
# TypeError: __code__ must be set to a code object
# TypeError: __code__ must be set to a code object
# TypeError: __code__ must be set to a code object
# TypeError: __code__ must be set to a code object
# TypeError: __code__ must be set to a code object
# TypeError: __code__ must be set to a code object
# TypeError: __code__ must be set to a code object
