import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

def add(a,b):
    return a+b

fptr = FUNTYPE(add)
print(fptr(2,4))

fptr = FUNTYPE(lambda a,b:a+b)
print(fptr(3,4))

# This is the C code that we want to call
CODE = """
int add(int a, int b) {
    return a+b;
}
"""

# Compile the C code into an object file
libname = tempfile.mktemp(".o")
open(libname,"w").write(CODE)
os.system("cc -c -o %s %s" % (libname,libname))

# Load the object into ctypes
lib = ctypes.CDLL(libname)

# Prepare the function prototype
lib.add.argtypes = (ctypes.c_int,ctypes.c_int)
lib.add.restype = ctypes.c_int

# Call the function
