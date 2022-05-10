import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.)
    y = ctypes.c_float(2.)
    z = ctypes.c_float(3.)

s = S()
vec = np.array([1.,1.,1.])

s.x = vec[0]
s.y = vec[1]
s.z = vec[2]

print(s.x)
np.array((s.x, s.y, s.z))
</code>
This produces no error message but it only sets the <code>x</code>, <code>y</code>, <code>z</code> components to the value of <code>x</code> component of the vector. The result is:
<code>1.0
array([ 1.,  1.,  1.], dtype=float32)
</code>
Can anyone help please?


A:

The problem is that all three elements in <code>vec</code> are equal (at least equal to machine precision). You can change the numbers in the next snippet to see that it works correctly
<code>&gt;&gt
