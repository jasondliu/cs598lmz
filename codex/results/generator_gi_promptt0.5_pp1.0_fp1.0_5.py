gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_frame
class G:
    def g(self):
        return sys._getframe()

g = G()
f = g.g()
f.f_back = gi.gi_frame
try:
    f.f_back.f_code
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test f.f_code.co_flags
f.f_code.co_flags = 0

# Test f.f_code.co_lnotab
f.f_code.co_lnotab = b'\x01\x01\x01\x01\x01\x01\x01\x01'

# Test f.f_code.co_stacksize
f.f_code.co_stacksize = 5

# Test f.f_code.co_names
f.f_code.co_names = ('a', 'b',
