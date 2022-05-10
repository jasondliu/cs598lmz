gi = (i for i in ())
# Test gi.gi_code.co_freevars and gi.gi_frame.f_locals.
if False:
    def g():
        y = 1
        yield
    gi = g()
    next(gi)

# The following was not present in the original PEP 380 (see issue #10644) but
# discussed on python-dev and added later to the documentation.
#
# There is a restriction for generators: if the code object passed to the
# generator's constructor is itself a generator, the code object of the
# subgenerator is used instead of that of the outer generator. This is a
# consequence of the optimization PEP 380 makes use of:
#
#     See Test gi.gi_code.co_freevars and gi.gi_frame.f_locals above.
#     Implementation note: When a generator is created, a reference to
#     its code object is acquired. If a subgenerator is created in a
#     generator's scope, the code object of the subgenerator is instead
#     acquired. This optimizes chained generators by avoiding that the
#     compiler creates a closure.

