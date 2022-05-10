fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
'''
Traceback (most recent call last):
  File "bug.py", line 71, in <module>
TypeError: 'code' property is read-only
'''
