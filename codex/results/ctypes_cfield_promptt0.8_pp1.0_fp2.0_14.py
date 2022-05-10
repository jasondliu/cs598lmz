import ctypes
# Test ctypes.CField instance.
# It was found that the __doc__ attribute was defined ctypes.CField.
# This is not read-only and this fact can be used to inject arbitrary code.
# Tested with Python 2.7.11 on Ubuntu 14.04 64-bit with gcc 4.8.4
# Tested with Python 2.7.11 on Windows 7 64-bit with VS 2008
# Tested with Python 3.5.1 on Ubuntu 14.04 64-bit with gcc 4.8.4
# Tested with Python 3.5.1 on Windows 7 64-bit with VS 2008

#include <stdio.h>
#include <stdlib.h>

// Run on Windows
#ifdef _WIN32
#define EXPORT extern "C" __declspec(dllexport)
#else
#define EXPORT extern "C"
#endif

EXPORT int function(int n) {
	printf("Number: %d\n", n);
	return 0;
}
'''

dll_file = 'poc.dll'

# Generate the DLL file.
with
