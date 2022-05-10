fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

class Restore:

    def __init__(self, old):
        self.old = old

    def __enter__(self):
        return self.old

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.excepthook = self.old

# We also test that sys.excepthook works at all, and so we have a way to
# check if it's been replaced with an uncooperative hook.

def test():
    def a():
        raise ValueError('foo')
    def b():
        a()

    sys.excepthook = malicious_excepthook

    with Restore(sys.excepthook):
        try:
            b()
        except ValueError:
            pass

    # This can never raise AssertionError, because malicious_excepthook
    # is a tail call
    assert sys.excepthook == malicious_excepthook
