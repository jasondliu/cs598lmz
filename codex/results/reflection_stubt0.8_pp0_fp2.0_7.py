fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# 2.
def fn(x):
    fn.a = x
    def g(y):
        nonlocal fn
        def h(z):
            nonlocal g
            def i(t):
                nonlocal h
                def j():
                    return fn.a, g.nonlocal.a, h.nonlocal.nonlocal.a, i.nonlocal.nonlocal.nonlocal.a
                return j
            return i
        return h
    return g

fn(1)(2)(3)(4)()

# 3.
def fn(x):
    fn.a = x
    def g(y):
        nonlocal fn
        g.a = y
        def h(z):
            nonlocal g
            h.a = z
            def i(t):
                nonlocal h
                i.a = t
                def j():
                    return fn.a, g.a, h.a, i.a
                return j 
            return i
        return h
    return g

fn(1)(2
