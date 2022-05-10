import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

# size should be 8
print "size of S = %d" % ctypes.sizeof(S)

# create pointer to S
s = ctypes.pointer(S())

# set x to 1
s.contents.x = 1

# set y to 2
s.contents.y = 2

# read x and y
assert s.contents.x == 1
assert s.contents.y == 2
</code>
Explanation:

<code>s = ctypes.pointer(S())</code> creates a pointer to struct <code>S</code> and initializes it to 0, which is equivalent to <code>s = ctypes.pointer(S(0, 0))</code>
<code>s.contents</code> accesses the pointed-to value, i.e., it is equivalent to <code>*s</code>
<code>s.contents.x</code> accesses field <code>x</code> of <code>*s</code>, i.
