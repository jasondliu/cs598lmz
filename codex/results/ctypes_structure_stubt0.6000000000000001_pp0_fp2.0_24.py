import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int64(1)
    y = ctypes.c_int64(2)
    z = ctypes.c_int64(3)

s = S()
a = ctypes.addressof(s)
print(ctypes.sizeof(s))
print(a)
print(a+1)
print(a+2)
print(a+3)
print(a+4)
print(a+5)
print(a+6)
print(a+7)
</code>
I was expecting the following output:
<code>24
140281897277088
140281897277089
140281897277090
140281897277091
140281897277092
140281897277093
140281897277094
140281897277095
</code>
but instead I get
<code>24
140281897277088
140281897277092
140281897277096
140281897277100
140281897277104

