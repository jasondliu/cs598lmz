fn = lambda: None
gi = (i for i in ())
fn.__code__ = F()
gi.__code__ = G()

attr_val = fn.__name__
attr_val1 = gi.__name__

attr_val2 = fn.__code__
attr_val3 = gi.__code__


def foo():
    pass

if __name__ == '__main__':
    foo()
    pass
