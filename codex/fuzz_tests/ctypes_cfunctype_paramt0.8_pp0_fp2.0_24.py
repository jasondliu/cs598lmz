import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p)
def on_stdout(block, x, y, w, h, str):
    print x, y, w, h, str
def on_stderr(block, x, y, w, h, str):
    sys.stderr.write('%.*s' % (len(str), str))

stdout_callback = FUNTYPE(on_stdout)
stderr_callback = FUNTYPE(on_stderr)

stdout_signal = FS_StdoutSignal(stdout_callback)
stderr_signal = FS_StdoutSignal(stderr_callback)
print dir(stderr_signal)
#sys.stdout.write('\033[?1049h')
#sys.stdout.write('\033[?1049l')
fs = FS_Terminal(80, 24, FS_NORMAL,
