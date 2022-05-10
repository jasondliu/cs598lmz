fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This test fails in 2to3 because the initial type of
# gi is an AST node, which is compared to an AST node
# in the code object. This is a problem because the
# AST node has an __eq__ method that always signals
# "not equal".
