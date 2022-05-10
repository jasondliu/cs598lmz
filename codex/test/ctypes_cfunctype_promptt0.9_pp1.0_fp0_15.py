import ctypes
# Test ctypes.CFUNCTYPE and ctypes.addressof
#
# this tests a problem on Windows where
# ctypes.addressof(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_short)(lambda x: x)(2))
# fails with a stack overflow, caused by the ctypes._CFuncPtr_call_python
# function, which calls PyThreadState_Swap, which swaps the current thread state
# with the one from the thread where the function was called from.  The second
# time this function is called, the thread state from the function has been
# swapped into the current thread, and all frames from that thread are gone.
#
# The reason is in PyThreadState_Swap: the global variable _PyThreadState_Current
# holds a pointer to the current thread state.  After a second call, the
# global variable is overwritten and cannot be restored, even if the previous
# value is saved into a local variable.
#
# The solution is to save _PyThreadState_Current (Python/ceval.c) globally, not
# on the per-thread state structure.
#

