gi = (i for i in ())
# Test gi.gi_code.co_flags and gi.gi_frame.f_code.co_flags
print(gi.gi_code.co_flags, gi.gi_frame.f_code.co_flags)

from test import support as t
df = t.run_doctest(t, '')

try:
    class C:
        for i in range(4):  # Test that it works in a class scope.
            pass
except:
    print('SKIP')
    raise SystemExit

# Test that the iterator can be unpacked
try:
    i1, i2, i3, i4 = C()
except:
    print('ERROR')
else:
    print('ok')
# Test that it is also true when iterating over the iterator
try:
    i1, i2, i3, i4 = iter(C())
except:
    print('ERROR')
else:
    print('ok')

# Test that the iterator can be unpacked with a stop value
try:
    i1, i2 = iter(C())
except:
    print('
