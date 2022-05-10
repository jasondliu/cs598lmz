import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)


class Timer(object):
    def __init__(self, interval, func, args=[], kwargs={}):
        self._timer = None
        self.interval = interval
        self.function = func
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


def test():
    def hello():
        print(1)
    t = Timer(1, hello)
    time.sleep(10)
    t.stop()


if __name__ == '__main
