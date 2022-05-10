fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Crash the interpreter by attempting to execute the generator
# object as code.
fn()

# The following line will not execute.
print("I'm still alive!")
