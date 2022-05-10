gi = (i for i in ())
# Test gi.gi_code
# TODO: does it ever make sense for this to not be the same as
# gi.__code__?
assert gi.__code__ is getattr(gi, "gi_code"), (
    "gi.gi_code should be the same as gi.__code__")
