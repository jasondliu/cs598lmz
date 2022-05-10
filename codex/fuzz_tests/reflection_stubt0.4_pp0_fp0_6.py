fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #3178
def f():
    def g():
        def h():
            return 'h'
        return h
    return g
f()()()

# issue #3179
def f():
    def g():
        def h():
            return 'h'
        return h
    return g
f()()()

# issue #3180
def f():
    def g():
        def h():
            return 'h'
        return h
    return g
f()()()

# issue #3181
def f():
    def g():
        def h():
            return 'h'
        return h
    return g
f()()()

# issue #3182
def f():
    def g():
        def h():
            return 'h'
        return h
    return g
f()()()

# issue #3183
def f():
    def g():
        def h():
            return 'h'
        return h
    return g
f()()()

# issue #3184
def f
