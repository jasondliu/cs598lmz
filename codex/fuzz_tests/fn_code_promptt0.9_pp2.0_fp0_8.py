fn = lambda: None
# Test fn.__code__.co_filename & fn.__code__.co_name
c1.f1(); c1.f2(); c1.f3()
c2.f1(); c2.f2(); c2.f3()

# Doesn't work:

def f5(x):
    print 5

def f6(x):
    print 6

## print f5.__class__.__name__
## print c1
