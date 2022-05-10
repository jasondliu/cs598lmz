fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Setup for infinite __reduce_ex__ loop
class A10:
    def __reduce__(self):
        return A10, ()

# Setup for infinite __reduce_ex__ recursion
class B10:
    def __reduce__(self):
        return B10, ()
    def __reduce_ex__(self, *args):
        return B10, ()

# Do the actual tests

dump_callables = (
    (complex(1j, 1), (complex, (0, 1))),
    (decimal.Decimal(1), (decimal.Decimal, ("1",))),
    #(dashiterable, TypeError  # XXX Have to fix this in dill
    (frozenset([2, 3]), (frozenset, ([2, 3],))),
    (fn, (fn.__class__, (from_pickle_import.module_code,))),
    (gi, TypeError),
    (iter((1, 2, 3)), (from_pickle_
