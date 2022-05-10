fn = lambda: None
gi = (i for i in ())
fn.__code__ = f.__code__
gi.gi_code = f.__code__

try:
    fn()
except Exception as e:
    print('fn() raises', e.__class__)
try:
    next(gi)
except Exception as e:
    print('next(gi) raises', e.__class__)

"""
<output>
fn() raises TypeError
next(gi) raises TypeError
</output>
"""
