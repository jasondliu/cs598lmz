gi = (i for i in ())
# Test gi.gi_code is None to distinguish from generators
# that were not created by the generator expression syntax
def genexpr(code, globs, locs=None):
    if not isinstance(code, types.CodeType):
        code = code.__code__
    if locs is None:
        locs = globs
    return types.GeneratorType(code, globs, locs)

# The following function is removed in Python 3.5.  It is
# used by the generator expression regression test.
def _gen_uses_closure(gen, names):
    """Return True iff the names used in the genexpr body are
    actually required in the closure."""
    body = gen.gi_code.co_consts[1]
    if isinstance(body, str):
        # Named genexps
        body = gen.gi_frame.f_globals[body]
    return any(name in body.co_freevars for name in names)

# From here on down, the code is the same for genexps and listcomps.
# This code is also used by the code
