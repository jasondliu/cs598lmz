fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

try:
    fn()
except TypeError as e:
    print(e)

try:
    fn.__code__ = gi
except TypeError as e:
    print(e)

try:
    fn()
except TypeError as e:
    print(e)
