fn = lambda: None
gi = (i for i in ())
fn.__code__ = c
gi.gi_code = c
gi.gi_yieldfrom = fn
gi.gi_running = False
sys.setprofile(lambda *args: None)
gi.__next__()

# Issue #25477: Crash when using a new-style class that overrides
# __contains__ with an __index__ method
class MyInt(int):
    def __index__(self):
        return 4
class MyInt2(int):
    __index__ = MyInt()
assert '12345678901234567890'[MyInt()] == '0'
assert '12345678901234567890'[MyInt2()] == '0'

a = array.array('i')

# Issue #25479: Crash on array.array.__setitem__
a[0:1] = [1 >> x for x in a]

# Issue #25481: Overflow checking was not correct: -1**2147483648
# was silently converted to 1
try:
    -1**2147483648
except TypeError:
    pass
