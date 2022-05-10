import ctypes
# Test ctypes.CField
# (It's a little like a variable, except that it is associated with a
# structure and its value is actually stored "in" that structure.)

class FIELD:
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

f = FIELD()

f.a = 3
f.b = 4

print "f.a = %i" % f.a
print "f.b = %i" % f.b

# Test ctypes.CField.__get__
# (It's like a property getter, but it's associated with a structure.
#  It's called automatically when the field is read.)

class FIELD2:
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    def a_get(self):
        print "FIELD2.a_get()"
        return self._a
    def a_set(self, value):
        print "FIELD2.a_set(%s)" % value
        self._
