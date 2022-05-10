fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'code' object is not iterable
# fn()
# File "test.py", line 7, in fn
# fn.__code__ = gi
# TypeError: readonly attribute
# fn()
# File "test.py", line 7, in fn
# fn.__code__ = gi
# TypeError: readonly attribute
# fn()
# File "test.py", line 7, in fn
# fn.__code__ = gi
# TypeError: readonly attribute
# fn()
# File "test.py", line 7, in fn
# fn.__code__ = gi
# TypeError: readonly attribute
# fn()
# File "test.py", line 7, in fn
# fn.__code__ = gi
# TypeError: readonly attribute
# fn()
# File "test.py", line 7, in fn
# fn.__code__ = gi
# TypeError: readonly attribute
# fn()
# File "test.py", line 7, in fn
# fn.__code__ = g
