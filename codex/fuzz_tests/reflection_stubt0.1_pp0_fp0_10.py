fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: segfault when __code__ is set to a non-code object
# that has a __call__ method.
class C:
    def __call__(self):
        pass

fn.__code__ = C()
fn()

# Issue #23897: segfault when __code__ is set to a non-code object
# that has a __call__ method.
class C:
    def __call__(self):
        pass

fn.__code__ = C()
fn()

# Issue #23897: segfault when __code__ is set to a non-code object
# that has a __call__ method.
class C:
    def __call__(self):
        pass

fn.__code__ = C()
fn()

# Issue #23897: segfault when __code__ is set to a non-code object
# that has a __call__ method.
class C:
    def __call__(self):
        pass

fn.__code__
