import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_int,ctypes.c_int,ctypes.c_int)

def py_func(a,b,c):
    print 'py_func',a,b,c

CMPFUNC = FUNTYPE(py_func)

dll = ctypes.cdll.LoadLibrary('dlltest.dll')
dll.func.argtypes = (ctypes.c_int,ctypes.c_int,FUNTYPE)
dll.func(1,2,CMPFUNC)
</code>
dlltest.dll:
<code>void __stdcall func(int a,int b,void (__stdcall *f)(int,int,int))
{
    f(a,b,a+b);
}
</code>
I have tried to use <code>__cdecl</code>, <code>__stdcall</code>, <code>__fastcall</code> and <code>__vectorcall</code> in both python and dll, but all of them can't work.

