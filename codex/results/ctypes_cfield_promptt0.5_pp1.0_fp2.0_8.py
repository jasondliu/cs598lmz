import ctypes
# Test ctypes.CField
import ctypes.test
ctypes.test.test_cfield()

# Test ctypes.util
import ctypes.util
ctypes.util.find_library("c")

# Test ctypes.wintypes
import ctypes.wintypes
ctypes.wintypes.BOOL

# Test sys.setdlopenflags()
import sys
sys.setdlopenflags(0)
sys.setdlopenflags(ctypes.RTLD_LOCAL)

# Test ctypes.create_string_buffer()
ctypes.create_string_buffer(0)
ctypes.create_string_buffer(1)
ctypes.create_string_buffer(1, "a")
ctypes.create_string_buffer(1, u"a")
ctypes.create_string_buffer(b"abc")
ctypes.create_string_buffer(u"abc")
ctypes.create_string_buffer(5, b"abc")
ctypes.create_string_buffer(5, u"abc")
ctypes.create_string_buffer(b"abc", 3)
