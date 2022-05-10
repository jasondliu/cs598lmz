import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p

s = S()
print s.x
s.x = None
print s.x
print

try:
    s.x = "abc"
except TypeError:
    print "Not allowed"
else:
    print "Allowed"
print

try:
    s.x = b"abc"
except TypeError:
    print "Not allowed"
else:
    print "Allowed"
</code>
Output:
<code>None
None

Not allowed

Allowed
</code>
This was tested under Python 2.7.3. I don't have Python 3.3 available to me at the moment, but from a quick reflection it looks like it still applies.

