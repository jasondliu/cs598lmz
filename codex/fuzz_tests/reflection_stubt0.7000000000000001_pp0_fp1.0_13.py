fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# test that lambdas can't be used as code objects
try:
    fn()
except TypeError:
    print("TypeError")
except Exception as e:
    print("Unexpected exception:", str(e))
else:
    print("No error")
