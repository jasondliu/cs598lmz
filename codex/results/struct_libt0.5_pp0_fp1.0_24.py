import _struct, _time, _thread

class _SigchldWatcher:
    def __init__(self):
        self.lock = _thread.allocate_lock()
        self.children = {}
        self.callbacks = {}
        self.sigchld_fd = _signal.sigchld_pipe()
        self.sigchld_fd_read = self.sigchld_fd[0]
        self.sigchld_fd_write = self.sigchld_fd[1]

    def __del__(self):
        # Close the pipe that we created.
        _os.close(self.sigchld_fd_read)
        _os.close(self.sigchld_fd_write)

    def _register_child(self, pid, callback):
        self.lock.acquire()
        self.children[pid] = callback
        self.lock.release()

    def _unregister_child(self, pid):
        self.lock.acquire()
        del self.children[pid]
        self
