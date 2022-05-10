fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi  # __code__ must be an instance of code

try:
    fn()
except RuntimeError:
    print("RuntimeError")
except TypeError:
    print("TypeError")
except:
    print("Unexpected error")
