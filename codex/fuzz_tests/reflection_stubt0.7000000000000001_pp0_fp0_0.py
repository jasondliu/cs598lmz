fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: None)()
fn.__code__.co_freevars = gi.gi_code.co_freevars = ()
fn.func_closure = gi.gi_frame.f_locals.func_closure = ()

# We can't use a regular generator with a closure, because then the
# generator would be a cell.  Cells can't be pickled because they have
# arbitrary python objects as their contents.
class _closing(object):
    def __init__(self, thing):
        self.thing = thing
    def __del__(self):
        self.thing.close()

class _GeneratorContextManager(object):
    """Helper for @contextmanager decorator."""

    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        try:
            return self.gen.__next__()
        except StopIteration:
            raise RuntimeError("generator didn't yield") from None

    def __exit__(self, type, value, traceback):

