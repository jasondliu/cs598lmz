import threading
# Test threading daemon mode
class Th(threading.Thread):
    def __init__(self):
        super(Th, self).__init__()
        self.daemon = True

    def run(self):
        print("I am sub thread, keep runing")

t = Th()
t.start()
print("{} :vars {}".format("I am main thread", vars(threading.currentThread())))
