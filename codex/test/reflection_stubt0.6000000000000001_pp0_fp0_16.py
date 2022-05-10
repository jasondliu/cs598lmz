fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# This is the expected result.

print(fn.__code__.co_filename)
print(fn.__code__.co_firstlineno)
print(fn.__code__.co_lnotab)
