import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

self.fptr = FUNTYPE(self.callback)
#self.fptr = self.callback

self.dll.addCallback(self.fptr)
</code>
However, when I call the callback from C++, it always returns an error code. If I call the function directly, it works as expected. What am I doing wrong?
EDIT:
The function is called like this:
<code>int i = cb(i);
</code>
I expect it to return 0. It doesn't.
EDIT2:
I tried this and got a segfault:
<code>typedef int(*callback_t)(int);

callback_t cb = (callback_t) callbacks[i];
int j = cb(i);
</code>


A:

You need to make the function callback work exactly like the C function pointer.
The C function pointer takes a <code>int</code> and returns an <code>int</code>.
The function callback must return an <code>int</code> and take
