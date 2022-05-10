import _struct

class _popen_cleanup:
    def __init__(self):
        self.pid = None
        self.pipe_handle = None
        self.pipe_read = None
        self.pipe_write = None
        self.pipe_close = None
        self.pipe_errread = None
        self.pipe_errwrite = None
        self.pipe_errclose = None
        self.pipe_errpipe = None
        self.read_handle = None
        self.write_handle = None
        self.read_close = None
        self.write_close = None
        self.err_read_handle = None
        self.err_write_handle = None
        self.err_read_close = None
        self.err_write_close = None
        self.err_pipe_handle = None
        self.err_pipe_close = None
        self.stdin_reader = None
        self.stdout_writer = None
        self.stderr_writer = None
        self.popen_handle = None
        self.popen_close = None
