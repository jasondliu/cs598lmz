fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the __code__ attribute can be set to a non-code object
# with a __call__ method.
class Foo:
    def __call__(self):
        pass

fn.__code__ = Foo()
fn()

# Test that the __code__ attribute can be set to a non-code object
# with a __call__ method and a __code__ attribute.
class Foo:
    def __call__(self):
        pass
    def __code__(self):
        pass

fn.__code__ = Foo()
fn()
