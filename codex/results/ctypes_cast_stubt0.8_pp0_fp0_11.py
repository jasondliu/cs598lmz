import ctypes
ctypes.cast(file_name, ctypes.c_char_p)
</code>


A:

I'm not sure what you mean by <code>'x'</code> and <code>'c'</code> - but you can use <code>ctypes.pointer()</code> to convert <code>ctypes</code> values to pointers accepted by the Windows API.
<code>#!python
# winapi_example.py
import os
import ctypes
from ctypes import wintypes

#Define Windows data types
LPSTR = ctypes.c_char_p
LPCSTR = ctypes.c_char_p
LPDWORD = ctypes.POINTER(ctypes.c_ulong)

#Get the function from the DLL
GetFileAttributesW = ctypes.windll.kernel32.GetFileAttributesW
GetFileAttributesW.argtypes = [LPCSTR]
GetFileAttributesW.restype = wintypes.DWORD

GetFileAttributes = ctypes.windll.kernel32.GetFileAttributesW   
GetFileAttributes.argtypes = [
