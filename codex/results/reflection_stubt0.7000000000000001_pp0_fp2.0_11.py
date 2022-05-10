fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Output:
# Traceback (most recent call last):
#   File "code-objects.py", line 58, in <module>
#     fn()
# TypeError: <generator object <lambda> at 0x7f68b731f1e0> is not a code object
