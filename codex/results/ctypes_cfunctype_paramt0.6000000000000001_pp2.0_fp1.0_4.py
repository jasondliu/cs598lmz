import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def _dummy_func():
    pass

def _make_func(name):
    return FUNTYPE(_dummy_func)

# These are the functions we actually want to wrap
_CALLBACK_FUNCS = [
    'PyOS_InputHook',
    'PyOS_ReadlineFunctionPointer',
    'PyOS_AddCloserFd',
    'PyOS_RemoveCloserFd',
    'PyOS_AfterFork',
    'PyEval_SetProfile',
    'PyEval_SetTrace',
    'PyEval_SetAsyncExc',
    'PyEval_GetAsyncExc',
    'PyEval_SetCoroutineAwaitCallback',
    'PyEval_SetCoroutineWrapper',
    'PyEval_SetAsyncGenFirstiterCallback',
    'PyEval_SetAsyncGenFinalizerCallback',
    'PyEval_SetAsyncGenValueWrapper',
    'PyEval_GetCoroutineAwaitCallback',
    'PyEval_GetCoroutineWrapper',
    '
