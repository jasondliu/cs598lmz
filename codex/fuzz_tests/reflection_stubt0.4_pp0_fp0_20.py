fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #17984: segfault on invalid __new__
class A(object):
    def __new__(cls):
        return super(A, cls).__new__(None)

# Issue #16650: segfault on invalid __init__
class B(object):
    def __new__(cls):
        return super(B, cls).__new__(cls)
    def __init__(self):
        super(B, self).__init__()

# Issue #16650: segfault on invalid __init__
class C(object):
    def __new__(cls):
        return super(C, cls).__new__(cls)
    def __init__(self):
        super(C, self).__init__()
        raise ValueError

# Issue #16650: segfault on invalid __init__
class D(object):
    def __new__(cls):
        return super(D, cls).__new__(cls)
    def
