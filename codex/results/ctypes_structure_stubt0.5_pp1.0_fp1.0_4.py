import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    y = ctypes.c_char_p

a = S()
a.x = "foo"
a.y = "bar"

b = S()
b.x = "baz"
b.y = "quux"

c = S()
c.x = "baz"
c.y = "quux"

print "a = ", a.x, a.y
print "b = ", b.x, b.y
print "c = ", c.x, c.y
print "a == b ? ", a == b
print "b == c ? ", b == c
</code>
Output:
<code>a =  foo bar
b =  baz quux
c =  baz quux
a == b ?  False
b == c ?  False
</code>

