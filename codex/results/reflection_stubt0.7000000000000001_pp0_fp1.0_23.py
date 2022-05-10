fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
l = list(fn.__code__)
try:
    fn()
except TypeError:
    pass
else:
    print('TypeError not raised')
try:
    l.append(0)
except TypeError:
    pass
else:
    print('TypeError not raised')

try:
    del l[0]
except TypeError:
    pass
else:
    print('TypeError not raised')

# from issue #23373
def f():
    pass

f.__code__ = 1

try:
    f()
except TypeError:
    pass
else:
    print('TypeError not raised')
