import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self, loop, on_start=None, on_stop=None, args=()):
        super().__init__()
        self.loop = loop
        self.on_start = on_start
        self.on_stop = on_stop
        self.args = args
        self.setDaemon(True)
    def run(self):
        if self.on_start:
            self.on_start(*self.args)
        while self.loop:
            time.sleep(1)
        if self.on_stop:
            self.on_stop(*self.args)

# Example class
class Test:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.timer = MyThread(True, self.timer_start, self.timer_end, (host, port))
    def start(self):
        self.timer.start()
    def timer_start(self, host, port):
        print("Timer Started for {}:{
