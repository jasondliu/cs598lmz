import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

class Protected(object):
    def __init__(self, callable_):
        self.callable = callable_
        self.wcb = None
        self.rcb = None

    def __call__(self, *args, **kwargs):
        if not self.wcb:
            self.wcb = FUNTYPE(self.write_callback)
            self.rcb = FUNTYPE(self.read_callback)

            self.original_stdin = os.fdopen(os.dup(sys.stdin.fileno()), 'r')
            self.original_stdout = os.fdopen(os.dup(sys.stdout.fileno()), 'w')

            self.pipe_r, self.pipe_w = os.pipe()
            self.pipe_r = os.fdopen(self.pipe_r, 'r')
            self.pipe_w = os.fdopen(self.pipe_w, 'w')

            self.stdout_buffer = []

