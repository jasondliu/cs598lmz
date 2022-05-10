import ctypes
# Test ctypes.CFUNCTYPE for memory management callback
# Looks like callbacks are released on exit() or so (emtpy list dllhandlers in pywintypes)
# PyMem_Free is called with NULL which crashes
#
# This is expected behaviour, since the callback is loaded in a dll and the
# python intepreter, or pywintypes, releases the dll. The callback is then
# released as well.
#
# However, it is possible to pass an 'external' callback to a dll, which
# will not be released on exit.
#
# Current ctypes implementation forces the python interpeter to release all
# callbacks, even if loaded in a dll. probably a bug
#
# Also, there is a memory leak, if the callback is passed to a dll, and then the
# dll is unloaded, the callback is not released.

