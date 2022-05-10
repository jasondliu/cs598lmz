fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# 100
# fn = lambda: None
# fn.__code__ = None
# fn()

# 101
# fn = lambda: None
# fn.__code__ = None
# fn()

# 102
# fn = lambda: None
# fn.__code__ = (i for i in ())
# fn()

# 103
# fn = lambda: None
# fn.__code__ = lambda: None
# fn()

# 104
# fn = lambda: None
# fn.__code__ = lambda: None
# fn()

# 105
# fn = lambda: None
# fn.__code__ = lambda: None
# fn()

# 106
# fn = lambda: None
# fn.__code__ = fn
# fn()

# 107
# fn = lambda: None
# fn.__code__ = fn
# fn()

# 108
# fn = lambda: None
# fn.__code__ = fn
# fn()

# 109
# fn = lambda: None
# fn.__code__ = fn
# fn
