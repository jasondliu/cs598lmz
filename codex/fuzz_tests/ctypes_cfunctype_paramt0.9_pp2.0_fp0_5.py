import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int32)

def doNothing(i):
    print('Do nothing with', i)

# convert your function to a C function that can be called by C
COURFUN = FUNTYPE(doNothing)

# call your C function
COURFUN(12)
</code>
From there you should be able to extend this to accept more complicated arguments.

