fn = lambda: None
# Test fn.__code__.co_argcount
class A:
    def __init__(self):
        pass
class B:
    def __init__(self, a):
        pass
class C:
    def __init__(self, a, b):
        pass
class D:
    def __init__(self, a, b, *c):
        pass
class E:
    def __init__(self, a, b, *c, **d):
        pass
class F:
    def __init__(self, a, b, *c, d, **e):
        pass
class G:
    def __init__(self, a, b, *, c):
        pass
class H:
    def __init__(self, a, b, *, c, **d):
        pass
class I:
    def __init__(self, a, b, *, c, d, **e):
        pass
class J:
    def __init__(self, a, b, c=1):
        pass
class K:
    def __init__(self, a,
