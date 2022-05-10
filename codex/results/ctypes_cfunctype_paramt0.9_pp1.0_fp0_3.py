import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def debugdumpcall(name):
    def _(x):
        import os
        import traceback
        print '%s:%s:%s' % (os.getpid(), name, x)
        traceback.print_stack()
    return FUNTYPE(_)
def debugdumpexec(name):
    def _(x):
        import os
        import traceback
        print '%s:%s:%s' % (os.getpid(), name, x)
        traceback.print_stack()
    return FUNTYPE(_)
def debugdumpsig(x):
    import os
    import traceback
    print '%s:sighandler:%s' % (os.getpid(), x)
    traceback.print_stack()
sigint = FUNTYPE(debugdumpsig)

import stdio
import libc
#libc = ctypes.cdll.LoadLibrary(None) # loads /usr/lib/libc.so.6
stdio.set_debug_info(debugdumpcall, debugdumpexec, debug
