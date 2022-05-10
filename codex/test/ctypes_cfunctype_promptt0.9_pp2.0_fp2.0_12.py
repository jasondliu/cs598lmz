import ctypes
# Test ctypes.CFUNCTYPE with a function that returns a pointer to a function.

# Uses the stdcall convention, because it's a Win32 convention and it's
# cleaner to use the same convention on all platforms.

import ctypes
from ctypes import wintypes

