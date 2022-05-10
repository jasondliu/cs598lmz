import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

@FUNTYPE
def fun(a, b):
    print("{} and {}".format(a, b))
    return a + b

def test_function(fun):
    print(fun(1, 2))

if __name__ == "__main__":
    test_function(fun)
</code>
Output:
<code>1 and 2
3
</code>

