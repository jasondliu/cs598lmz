import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
class CField(ctypes.CField):
    def _check_retval_(self, retval):
        if retval & 1 == 0:
            print "Failed: retval = %d" % retval
            raise ValueError, "Bad value"
        return retval & ~1
    def _check_param_(self, value):
        if value & 1:
            print "Failed: value = %d" % value
            raise ValueError, "Bad value"
        return value

S.x = CField(S.x)

s = S()
s.x = 100
print s.x
s.x = 101
</code>


A:

In your <code>_check_retval_</code> method, <code>self</code> is a member of <code>ctypes.CField</code>, not a member of your subclass.  You need to get the value from <code>self</code>'s parent class.  You need something like this:
<code>def _check_retval_(self, retval):
    class_type
