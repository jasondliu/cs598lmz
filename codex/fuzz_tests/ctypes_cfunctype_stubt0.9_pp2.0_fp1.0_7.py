import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
def f():
    f()

# Disable cache for these tests
def make_instruction_sequence(func):
    return func.func_code

def make_frame(func, args=tuple(), kwds={}, closure=None, local_vars={}):
    seq = make_instruction_sequence(func)
    frame = frame_new(None, *seq)
    frame.set_local_args(*args)
    frame.set_local_kwds(kwds)
    frame.set_locals(local_vars)
    frame.set_acclo(closure)
    return frame

def c_getlocal_r(frame, idx):
    val = ctypes.c_int.in_dll(runner_dll, 'local_vars')
    return pypy_asm_malloc_varsize_box(frame.get_locals())

def py_getlocal_r(frame, idx):
    return frame.get_locals()

def c_setlocal_r(frame, idx,
