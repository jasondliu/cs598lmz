import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(i, j):
    print i,j
    return 1

def main():
    libfile = ctypes.util.find_library('libtest')
    if libfile == None:
        raise Exception("error: unable to find libtest")
    lib = ctypes.CDLL(libfile)

    cb = FUNTYPE(callback)
    lib.test(cb)

if __name__ == '__main__':
    main()
</code>
compiling and running this code I get the following error:
<code>error: unable to find libtest
</code>


A:

You have to specify the library path.
The following script works:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(i, j):
    print i,j
    return 1

def main():
    libfile = "/home/
