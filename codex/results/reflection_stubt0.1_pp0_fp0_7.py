fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18097: crash when __code__ is set to a non-code object
# with a __call__ method.
class Callable:
    def __call__(self):
        pass

fn.__code__ = Callable()
fn()

# Issue #18097: crash when __code__ is set to a non-code object
# with a __call__ method.
class Callable:
    def __call__(self):
        pass

fn.__code__ = Callable()
fn()

# Issue #18097: crash when __code__ is set to a non-code object
# with a __call__ method.
class Callable:
    def __call__(self):
        pass

fn.__code__ = Callable()
fn()

# Issue #18097: crash when __code__ is set to a non-code object
# with a __call__ method.
class Callable:
    def __call__(self):
        pass

fn.__code__ = Callable()
fn()


