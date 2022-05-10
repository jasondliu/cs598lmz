import ctypes
# Test ctypes.CFUNCTYPE

if __name__ == '__main__':
    from ctypes import *
    from ctypes.wintypes import *

    # Get the function pointer
    GetModuleHandle = windll.kernel32.GetModuleHandleA
    GetModuleHandle.restype = HMODULE

    # Create the prototype
    prototype = CFUNCTYPE(HMODULE, c_char_p)

    # Create the function
    GetModuleHandle2 = prototype(("GetModuleHandleA", windll.kernel32))

    # Test it
    print GetModuleHandle2(None)
    print GetModuleHandle(None)
