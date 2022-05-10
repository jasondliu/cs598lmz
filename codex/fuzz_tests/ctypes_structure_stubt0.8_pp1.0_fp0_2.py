import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

arr = (S*4)()

for idx, v in enumerate(arr):
    v.x = idx + 0.1
    v.y = idx + 0.2
    v.z = idx + 0.3

darr = np.ctypeslib.as_array(arr, (4,3))

print("tolist:")
print(darr.tolist())
print("view:")
print(darr.view(np.float64))
</code>
Output:
<code>tolist:
[[0.1, 0.2, 0.3], [1.1, 1.2, 1.3], [2.1, 2.2, 2.3], [3.1, 3.2, 3.3]]
view:
[[0. 1. 2. 3.]
 [0.1 0.2 0.3 1.1 1.2 1.3]
 [2.1 2.2
