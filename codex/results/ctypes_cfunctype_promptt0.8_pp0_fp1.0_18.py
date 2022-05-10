import ctypes
# Test ctypes.CFUNCTYPE().
# test_types_gen.py: CFUNCTYPE(..., ...)
# http://docs.python.org/dev/library/ctypes.html#ctypes._CFuncPtr

try:
	ctypes.CFUNCTYPE
except AttributeError:
	print('SKIP')
	raise SystemExit

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa383751(v=vs.85).aspx
#
# BOOL WINAPI WriteFile(
#   __in         HANDLE hFile,
#   __in         LPCVOID lpBuffer,
#   __in         DWORD nNumberOfBytesToWrite,
#   __out_opt    LPDWORD lpNumberOfBytesWritten,
#   __inout_opt  LPOVERLAPPED lpOverlapped
# );
#
# Note that OVERLAPPED is a struct, and structs are passed by pointer, so
# this should be a pointer to the struct, or a pointer to a pointer to the
# struct.

Write
