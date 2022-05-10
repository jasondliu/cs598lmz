fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError, but it doesn't.
# See https://bugs.python.org/issue29092
#
# Traceback (most recent call last):
#   File "./test_code_object.py", line 12, in <module>
#     fn()
# TypeError: 'generator' object is not callable
