import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class Arr(ctypes.Structure):
    _fields_ = [('n', ctypes.c_int), ('arr', ctypes.POINTER(S))]

s = S(1,2)

# put some ctypes pointers in the array
arr = Arr(2, ctypes.pointer(s))

# marshalling the array
a = (Arr * 2)()
a[0] = arr
a[1] = arr

# save the array to a file
file("test.bin", "wb").write(a)

# read the file and check it
b = (Arr * 2).from_file("test.bin")
print 'a == b : ', a == b
</code>
You get the exception that the file cannot be read. Using the <code>__len__</code> function is a way to tell how many items to read, but maybe it can be simplified (It's a bit ugly)

