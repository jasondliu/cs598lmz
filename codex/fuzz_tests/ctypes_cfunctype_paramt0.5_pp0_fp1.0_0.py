import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

@FUNTYPE
def func(a,b,c,d):
    print "a = %d, b = %d, c = %d, d = %d" % (a,b,c,d)
    return a+b+c+d

func(1,2,3,4)
</code>
Output:
<code>a = 1, b = 2, c = 3, d = 4
</code>

