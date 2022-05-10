import ctypes
# Test ctypes.CField.
import ctypes.test
assert ctypes.test.test_field()
# Test PyCObject.
import ctypes.test.cobject
assert ctypes.test.cobject.test()
# Test ctypes.util.
import ctypes.util
# ctypes.util.find_library()
assert ctypes.util.find_library("c")
# Test ctypes.wintypes.
import ctypes.wintypes
assert ctypes.wintypes.HANDLE(0)
assert ctypes.wintypes.HWND(0)
assert ctypes.wintypes.LPARAM(0)
assert ctypes.wintypes.LPVOID(0)
assert ctypes.wintypes.LRESULT(0)
assert ctypes.wintypes.WPARAM(0)
