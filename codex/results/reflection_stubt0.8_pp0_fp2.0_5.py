fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Crash or Proper error:
# fn()

# Valid Python:

fn.__code__ = None
fn()

class Class:
    def __call__(self):
        pass

fn.__code__ = Class()

# Crash or Proper error:
# fn()
