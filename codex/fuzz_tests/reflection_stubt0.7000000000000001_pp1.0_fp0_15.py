fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

#run the test
try:
    fn()
except TypeError:
    print("TypeError")
