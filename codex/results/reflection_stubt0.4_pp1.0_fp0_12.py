fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This is the same as above, but the generator is created before
# the function object.
gi = (i for i in ())
fn = lambda: None
fn.__code__ = gi
fn()

# This is the same as above, but the generator is created before
# the function object, and the function object is created before
# the code object.
gi = (i for i in ())
fn = lambda: None
fn.__code__ = types.FunctionType(gi, {}, 'fn')
fn()

# This is the same as above, but the generator is created before
# the function object, and the function object is created before
# the code object, and the code object is created before the
# function object.
gi = (i for i in ())
fn = lambda: None
fn.__code__ = types.FunctionType(types.FunctionType(gi, {}, 'fn').__code__, {}, 'fn')
fn()

# This is the same as above, but the generator is created before
# the function object, and the function object is created before

