import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def testfunction(n):
    print("Hello from python!")
    return n*n

def main():
    # This is where we call the function and give it the function pointer
    # to the testfunction
    func = FUNTYPE(testfunction)
    print("result =", func(5))

if __name__=="__main__":
    main()
</code>

