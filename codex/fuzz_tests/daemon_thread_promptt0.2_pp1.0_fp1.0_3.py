import threading
# Test threading daemon
# https://docs.python.org/3.6/library/threading.html#thread-objects

class ThreadingDaemon(threading.Thread):
    def __init__(self, name, daemon=True):
        super(ThreadingDaemon, self).__init__()
        self.name = name
        self.daemon = daemon
        self.start()

    def run(self):
        while True:
            print("{} is running".format(self.name))
            time.sleep(1)

if __name__ == "__main__":
    ThreadingDaemon("ThreadingDaemon")
    time.sleep(5)
    print("Main thread exit")
