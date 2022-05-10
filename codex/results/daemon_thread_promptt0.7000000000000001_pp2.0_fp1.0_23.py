import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html
class LoopingCall(threading.Thread):
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.daemon = True

    def run(self):
        while True:
            self.func(*self.args, **self.kwargs)
            time.sleep(1)


def print_stuff():
    print('stuff')

t = LoopingCall(print_stuff)
t.start()
</code>

