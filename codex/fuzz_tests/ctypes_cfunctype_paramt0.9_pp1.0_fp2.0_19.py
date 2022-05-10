import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_int,ctypes.c_int) #this line is critical for 64 bit version
WkEventHandler = FUNTYPE(wkcallback)

IM_AT_DESTROY = 2 #this is a hardwired define from WK.pas

#global variables
global WkOBJ
global WKEventHandler
global WkDestroyEventHandler


#trampoline functions
def tr_onPrevious(curPage,prevPage):
    global WinForm #this has to be global here, in other cases just pass WinForm as argument to the callback invocation below
    WinForm.onPrevious(curPage,prevPage)
def tr_onNext(curPage,nextPage):
    global WinForm
    WinForm.onNext(curPage,nextPage)
def tr_onEntry(curPage,prevPage):
    global WinForm
    WinForm.onEntry(curPage,prevPage)
def tr_onExit(curPage,prevPage):
    global WinForm
    WinForm.onExit(curPage,prevPage)
def tr_onClose(
