fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test for bug #1465702: crash if __code__ is not a code object
def f(): pass
f.__code__ = 1
f()

# Test for bug #1549593: crash if __call__ is not a PyCFunction
class C:
    def __call__(self):
        return 1
C.__call__ = 2
print(C()())

# Test for bug #1549593: crash if __call__ is not a PyCFunction
class C:
    def __call__(self):
        return 1
C.__call__ = C.__call__.__get__(C())
print(C()())

# Test for bug #1549593: crash if __call__ is not a PyCFunction
class C:
    def __call__(self):
        return 1
C.__call__ = C.__call__.__get__(C)
print(C()())

# Test for bug #1549593: crash if __call__ is not a PyCFunction
class C:
    def __call__
