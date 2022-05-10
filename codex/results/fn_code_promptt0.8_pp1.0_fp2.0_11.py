fn = lambda: None
# Test fn.__code__.co_argcount
print fn.__code__.co_argcount
fn.__code__.co_argcount = 4
'''
# output
0
Traceback (most recent call last):
  File "test.py", line 6, in ?
    fn.__code__.co_argcount = 4
AttributeError: readonly attribute
'''
