import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64)

lib = ctypes.CDLL("./libnchash.so")
lib.nchash_h64.argtypes= (ctypes.c_uint64,ctypes.c_uint64)
lib.nchash_h64.restype= ctypes.c_uint64

h64 = FUNTYPE(lib.nchash_h64)

key,value = (1,1)

print lib.nchash_h64(key,value)
print h64(key,value)
</code>
My c code is:
<code>#include "Python.h"
#include&lt;stdio.h&gt;
#include&lt;stdint.h&gt;
#include&lt;stdlib.h&gt;

uint64_t nchash_h64(uint64_t key, uint64_t value) {
    uint64_t hash = 0xcbf29ce484222325ull;
    /* key
