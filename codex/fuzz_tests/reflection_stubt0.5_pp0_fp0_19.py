fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should be a TypeError, not a SystemError.
# See http://bugs.python.org/issue13429
class C(object):
    def __call__(self):
        pass
C().__call__.__code__ = gi
C()()
