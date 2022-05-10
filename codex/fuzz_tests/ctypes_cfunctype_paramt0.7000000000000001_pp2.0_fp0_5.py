import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
Add = FUNTYPE(('Add', lib))
print(Add(5, 12))
</code>
Output:
<code>17
</code>
The function definition in the .h file is:
<code>int Add(int a, int b);
</code>
The function definition in the .cpp file is:
<code>extern "C" int Add(int a, int b) {
    return a + b;
}
</code>
My question is: Is there any way to make this code work without the need for <code>extern "C"</code> in the cpp file?

