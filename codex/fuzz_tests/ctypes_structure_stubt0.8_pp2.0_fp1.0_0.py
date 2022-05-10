import ctypes

class S(ctypes.Structure):
    x = 1
    y = 2
    z = [3, 4]

print(S.z)
print(S.z[0])
&gt;&gt;&gt; c_int(3)
&gt;&gt;&gt; 3
</code>

