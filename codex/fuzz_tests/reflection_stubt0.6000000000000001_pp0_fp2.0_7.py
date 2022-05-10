fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'function'

# test
print(fn())

# output
# Traceback (most recent call last):
#  File "./test_fn.py", line 20, in <module>
#    print(fn())
# TypeError: 'generator' object is not callable
