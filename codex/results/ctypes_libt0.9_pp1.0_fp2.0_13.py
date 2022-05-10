import ctypes
ctypes.c_int.in_dll(lib, "two").value

# 2
</code>
What's in the source do I have to change to make the values I've modified work, especially in a loop?


A:

To solve the problem of variable updates, I've resorted to changing line 11 in cpp_files/main.cpp:
<code>const int two = 7;
</code>
to
<code>#include &lt;stdlib.h&gt;
int two = 7;
</code>
As you can see, it's obviously possible to change values through CFFI now:
<code>In [1]: import cffi

In [2]: ffi=cffi.FFI()

In [3]: ffi.cdef("""
   ...: int add(int a, int b);
   ...: int sub(const int a, const int b);
   ...: 
   ...: const int one;
   ...: extern int two;
   ...: """)

In [4]: lib = ffi.dlopen("./cpp_files
