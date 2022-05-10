import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_long)

def set_callback(f):
    return FUNTYPE(f)

lib = ctypes.cdll.LoadLibrary('../bin/a.out')

def callback(x):
    print("Calling back with {0}".format(x))
    return x

lib.SetCallback.argtypes = ctypes.c_void_p,
lib.SetCallback.restype = ctypes.c_void_p

lib.ExecuteCallback()

lib.SetCallback(set_callback(callback))

lib.ExecuteCallback()
</code>
I'm getting the error:
<code>TypeError: a float is required
</code>
I've tried declaring the C callback to return a <code>unsigned long</code> instead of a <code>long</code>, but that didn't change the output or behaviour.
Here is the C code:
<code>// safe_fun_ptr.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include &lt
