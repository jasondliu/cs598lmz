fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16078: crash when __code__ is set to a non-code object
# with a __call__ method.
class C:
    def __call__(self):
        pass

def f():
    pass

f.__code__ = C()
f()

# Issue #16078: crash when __code__ is set to a non-code object
# with a __call__ method.
class C:
    def __call__(self):
        pass

def f():
    pass

f.__code__ = C()
f()

# Issue #16078: crash when __code__ is set to a non-code object
# with a __call__ method.
class C:
    def __call__(self):
        pass

def f():
    pass

f.__code__ = C()
f()

# Issue #16078: crash when __code__ is set to a non-code object
# with a __call__ method.
class C:
    def __call__(self):
       
