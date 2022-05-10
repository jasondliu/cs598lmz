fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

print('-'*75, '\n')

def f():
    # f.__code__ = (x for x in ())
    f.__code__ = 1
f()

print('-'*75, '\n')

def f():
    # f.__code__ = (x for x in ())
    f.__code__ = 1
    f.__code__ = (x for x in ())
f()

print('-'*75, '\n')

def f():
    f.__code__ = (x for x in ())
    f.__code__ = 1
    f.__code__ = (x for x in ())
    def g():
        pass
f()

print('-'*75, '\n')

def f():
    f.__code__ = (x for x in ())
    f.__code__ = 1
    f.__code__ = (x for x in ())
    def g():
        pass
    g()
f()

print('-'*75, '\n')


