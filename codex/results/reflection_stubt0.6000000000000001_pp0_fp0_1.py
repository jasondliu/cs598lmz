fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__.co_flags

def fn():
    pass
fn.__code__.co_flags

def fn():
    def inner():
        pass
    inner()
fn.__code__.co_flags

def fn():
    def inner():
        def inner2():
            pass
        inner2()
    inner()
fn.__code__.co_flags

def fn():
    def inner():
        def inner2():
            pass
        return inner2()
    return inner()
fn.__code__.co_flags

def fn():
    def inner():
        def inner2():
            pass
        return inner2()
    inner()
fn.__code__.co_flags

def fn():
    def inner():
        def inner2():
            pass
        return inner2
    inner()
fn.__code__.co_flags

def fn():
    def inner():
        def inner2():
            pass
        return inner2
    inner()()
fn.__code__.co_flags

def fn
