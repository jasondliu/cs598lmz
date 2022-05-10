import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_byte)

class _loop(object):
    def __init__(self):
        self.running = True

    def run(self):
        self.running = True
        self._run()

    def stop(self):
        self.running = False
        self._stop()

    def _run(self):
        raise NotImplementedError

    def _stop(self):
        raise NotImplementedError

class _poll(_loop):
    def __init__(self, fdset, timeout=None):
        super(_poll, self).__init__()
        self.fdset = fdset
        self.timeout = timeout

    def _run(self):
        while self.running:
            self.fdset.poll(self.timeout)

class _signal(_loop):
    def __init__(self, sigset):
        super(_signal, self).__init__()
        self.sigset = sigset

    def _run(self):
        while self.running:
            self.sigset.s
