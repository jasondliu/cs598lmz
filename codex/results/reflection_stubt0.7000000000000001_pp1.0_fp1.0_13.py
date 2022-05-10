fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError:
    print('TypeError')

# __class__ should be ignored by the code object
try:
    def fn():
        pass
    fn.__code__ = int
    fn()
except TypeError:
    print('TypeError')
