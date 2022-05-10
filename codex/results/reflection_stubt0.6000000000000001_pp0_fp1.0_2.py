fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# method
# https://docs.python.org/3.6/reference/datamodel.html#the-standard-type-hierarchy

# function
# https://docs.python.org/3.6/library/functions.html#func-instancemethod

# generator
# https://docs.python.org/3.6/reference/expressions.html#generator-expressions
