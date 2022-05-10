import ctypes
ctypes.cast(x, ctypes.py_object).value

# load ctypes dll
mydll = ctypes.WinDLL("DLL")

# call function within ctypes dll
def connect(port):
    return mydll.ScanPorts(port)
</code>
output:
<code>True
</code>
dll function def:
<code>extern "C" DLL_API BOOL __cdecl ScanPorts(int input) {
    cerr &lt;&lt; "\n\ncaller is " &lt;&lt; input &lt;&lt; "\n\n";
    return TRUE;
}
</code>

