fn = lambda: None
gi = (i for i in ())
fn.__code__ = (1, 1, 1, 'c', ()[:], gi, (1, 2, 3), 0, '', (), (), ())
fn.__globals__['foo'] = fn
sys.exit(fn.__code__.co_freevars[0].__reduce_ex__(4))
